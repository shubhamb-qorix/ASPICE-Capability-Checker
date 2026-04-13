"""
ASPICE RAG Engine — builds and queries the ASPICE v4.0 knowledge base.

Embedding backend (in priority order):
  1. sentence-transformers + FAISS  (requires download of all-MiniLM-L6-v2)
  2. sklearn TF-IDF + cosine similarity  (zero-download fallback, always available)

LLM generation (optional):
  * GPT-4o via OpenAI when OPENAI_API_KEY is set
  * Built-in rule-based response otherwise
"""

from __future__ import annotations

import os
import re
from typing import Any

import numpy as np

# Small value added to vector norms to prevent division by zero during normalisation
_EPSILON = 1e-9

from .aspice_knowledge import (
    ASSESSMENT_QUESTIONS,
    CAPABILITY_LEVELS,
    LEVEL_ACHIEVEMENT_RULES,
    PROCESS_GROUPS,
    RATING_SCALE,
)

# ---------------------------------------------------------------------------
# Optional OpenAI client
# ---------------------------------------------------------------------------

_openai_client = None


def _init_openai() -> None:
    global _openai_client
    api_key = os.getenv("OPENAI_API_KEY", "")
    if api_key and _openai_client is None:
        from openai import OpenAI
        _openai_client = OpenAI(api_key=api_key)


# ---------------------------------------------------------------------------
# Document builder
# ---------------------------------------------------------------------------


def _build_knowledge_documents() -> list[dict[str, str]]:
    """Convert ASPICE knowledge structures into flat text chunks for retrieval."""
    docs: list[dict[str, str]] = []

    for level, data in CAPABILITY_LEVELS.items():
        text = (
            f"ASPICE v4.0 Capability Level {level}: {data['name']}\n"
            f"Description: {data['description']}\n"
        )
        for pa in data.get("process_attributes", []):
            text += (
                f"\nProcess Attribute {pa['id']} — {pa['name']}:\n"
                f"{pa['description']}\n"
                "Indicators:\n"
                + "\n".join(f"  * {i}" for i in pa["indicators"])
                + "\n"
            )
        docs.append({"id": f"CL_{level}", "content": text, "type": "capability_level"})

    for pa_id, questions in ASSESSMENT_QUESTIONS.items():
        text = (
            f"Assessment Questions for {pa_id}:\n"
            + "\n".join(f"  {i+1}. {q}" for i, q in enumerate(questions))
        )
        docs.append({"id": f"Q_{pa_id.replace(' ', '_')}", "content": text, "type": "questions"})

    for group_id, group in PROCESS_GROUPS.items():
        for proc_id, proc in group["processes"].items():
            text = (
                f"ASPICE Process {proc_id} - {proc['name']} (Group: {group['name']})\n"
                f"Purpose: {proc['purpose']}\n\n"
                "Outcomes:\n" + "\n".join(f"  * {o}" for o in proc["outcomes"]) + "\n\n"
                "Work Products:\n" + "\n".join(f"  * {w}" for w in proc["work_products"]) + "\n\n"
                "Base Practices:\n" + "\n".join(f"  * {b}" for b in proc["base_practices"]) + "\n"
            )
            docs.append({"id": proc_id, "content": text, "type": "process"})

    text = "ASPICE Rating Scale (ISO/IEC 33020):\n"
    for code, info in RATING_SCALE.items():
        text += f"  {code} - {info['name']} ({info['range']})\n"
    docs.append({"id": "RATING_SCALE", "content": text, "type": "rating"})

    text = "ASPICE Capability Level Achievement Rules:\n"
    for lvl, rule in LEVEL_ACHIEVEMENT_RULES.items():
        text += f"\nLevel {lvl} Requirements:\n"
        for pa, ratings in rule.get("required_ratings", {}).items():
            text += f"  {pa}: must be {' or '.join(ratings)}\n"
    docs.append({"id": "LEVEL_RULES", "content": text, "type": "rules"})

    return docs


# ---------------------------------------------------------------------------
# TF-IDF vector store (zero-download fallback)
# ---------------------------------------------------------------------------


class _TfidfVectorStore:
    """Lightweight TF-IDF retriever using scikit-learn."""

    def __init__(self) -> None:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        self._vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.95, ngram_range=(1, 2))
        self._cosine = cosine_similarity
        self._docs: list[dict[str, str]] = []
        self._matrix: Any = None

    def build(self, docs: list[dict[str, str]]) -> None:
        self._docs = docs
        self._matrix = self._vectorizer.fit_transform([d["content"] for d in docs])

    def search(self, query: str, top_k: int = 5) -> list[dict[str, str]]:
        if self._matrix is None:
            return []
        scores = self._cosine(self._vectorizer.transform([query]), self._matrix)[0]
        return [self._docs[i] for i in scores.argsort()[::-1][:top_k]]


# ---------------------------------------------------------------------------
# Neural store (sentence-transformers + FAISS) — optional
# ---------------------------------------------------------------------------


def _try_build_neural_store(docs: list[dict[str, str]]) -> Any | None:
    """Build a FAISS neural store; return None if model is unavailable."""
    try:
        import faiss
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer("all-MiniLM-L6-v2")
        texts = [d["content"] for d in docs]
        emb = model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
        norm = emb / (np.linalg.norm(emb, axis=1, keepdims=True) + _EPSILON)
        index = faiss.IndexFlatIP(emb.shape[1])
        index.add(norm.astype(np.float32))

        class _NeuralStore:
            def __init__(self, _docs, _model, _index):
                self._docs = _docs
                self._model = _model
                self._index = _index

            def build(self, docs):
                pass

            def search(self, query, top_k=5):
                q = self._model.encode([query], show_progress_bar=False, convert_to_numpy=True)
                q = (q / (np.linalg.norm(q, axis=1, keepdims=True) + _EPSILON)).astype(np.float32)
                _, indices = self._index.search(q, top_k)
                return [self._docs[i] for i in indices[0] if i < len(self._docs)]

        return _NeuralStore(docs, model, index)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Unified vector store
# ---------------------------------------------------------------------------


class AspiceVectorStore:
    """
    Hybrid vector store: tries neural embeddings first, falls back to TF-IDF.
    """

    def __init__(self) -> None:
        self._backend: Any = None

    def build(self, docs: list[dict[str, str]]) -> None:
        neural = _try_build_neural_store(docs)
        if neural is not None:
            self._backend = neural
        else:
            self._backend = _TfidfVectorStore()
            self._backend.build(docs)

    def search(self, query: str, top_k: int = 5) -> list[dict[str, str]]:
        if self._backend is None:
            return []
        return self._backend.search(query, top_k=top_k)


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------


def _generate_response(prompt: str, context: str) -> str:
    _init_openai()
    if _openai_client:
        system = (
            "You are an expert ASPICE v4.0 assessor and consultant. "
            "Answer questions about ASPICE process capability levels, process attributes, "
            "base practices, work products, and assessment guidance based strictly on the "
            "ASPICE v4.0 standard. Be precise, structured, and practical."
        )
        user = f"Context from ASPICE v4.0 knowledge base:\n\n{context}\n\nQuestion: {prompt}"
        resp = _openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.2,
            max_tokens=1500,
        )
        return resp.choices[0].message.content or ""

    return (
        "**ASPICE Knowledge Base Answer** (set OPENAI_API_KEY for AI-generated responses)\n\n"
        + context
    )


# ---------------------------------------------------------------------------
# Capability Level Assessment Engine
# ---------------------------------------------------------------------------


def assess_capability_level(pa_ratings: dict[str, str]) -> dict[str, Any]:
    """
    Determine the achieved capability level from a dict of PA ratings.

    Per ISO/IEC 33020 §7.4: evaluate each level independently and return
    the *highest* level whose requirements are fully met.

    Parameters
    ----------
    pa_ratings : dict mapping PA ID (e.g. "PA 1.1") -> rating letter ("N"/"P"/"L"/"F")

    Returns
    -------
    dict with keys: achieved_level, level_name, level_description,
                    gaps, recommendations, pa_details
    """
    pa_ratings = {k.upper(): v.upper() for k, v in pa_ratings.items()}

    achieved_level = 0
    all_gaps: dict[int, list[str]] = {}

    for level in range(1, 6):
        rule = LEVEL_ACHIEVEMENT_RULES.get(level, {})
        required = rule.get("required_ratings", {})
        level_ok = True
        level_gaps: list[str] = []

        for pa, allowed in required.items():
            actual = pa_ratings.get(pa, "N")
            if actual not in allowed:
                level_ok = False
                level_gaps.append(
                    f"Level {level}: {pa} is '{actual}' but needs to be "
                    f"'{' or '.join(allowed)}' - currently rated: {RATING_SCALE[actual]['name']}"
                )

        if level_ok:
            achieved_level = level
        else:
            all_gaps[level] = level_gaps

    gaps: list[str] = all_gaps.get(achieved_level + 1, [])

    recommendations: list[str] = []
    for gap in gaps:
        m = re.search(r"(PA \d+\.\d+)", gap)
        if m:
            pa = m.group(1)
            if pa in ASSESSMENT_QUESTIONS:
                recommendations.append(
                    "To improve " + pa + ", address: " + ASSESSMENT_QUESTIONS[pa][0]
                )

    pa_details: list[dict[str, str]] = []
    for pa_id, rating in pa_ratings.items():
        info = RATING_SCALE.get(rating, RATING_SCALE["N"])
        pa_details.append({
            "pa": pa_id,
            "rating": rating,
            "rating_name": info["name"],
            "range": info["range"],
        })

    level_info = CAPABILITY_LEVELS.get(achieved_level, CAPABILITY_LEVELS[0])
    return {
        "achieved_level": achieved_level,
        "level_name": level_info["name"],
        "level_description": level_info["description"],
        "gaps": gaps,
        "recommendations": recommendations,
        "pa_details": pa_details,
    }


# ---------------------------------------------------------------------------
# Main RAG Agent
# ---------------------------------------------------------------------------


class AspiceAgent:
    """
    ASPICE v4.0 RAG agent.

    Features
    --------
    * Retrieval-Augmented Generation over ASPICE v4.0 knowledge base
    * Capability level assessment from PA ratings (ISO/IEC 33020)
    * Process-specific guidance (outcomes, work products, base practices)
    * Knowledge enhancement: stores and queries custom organisational notes
    * Interactive Q&A via chat()
    * Hybrid embedding backend: neural (sentence-transformers) or TF-IDF
    """

    def __init__(self) -> None:
        self._store = AspiceVectorStore()
        self._custom_docs: list[dict[str, str]] = []
        self._built = False
        self._history: list[dict[str, str]] = []

    def build_knowledge_base(self) -> None:
        """Build the vector index from the bundled ASPICE knowledge."""
        docs = _build_knowledge_documents() + self._custom_docs
        self._store.build(docs)
        self._built = True

    def add_custom_knowledge(self, text: str, doc_id: str = "") -> None:
        """Add organisation-specific knowledge to enhance the agent."""
        idx = doc_id or f"CUSTOM_{len(self._custom_docs)}"
        self._custom_docs.append({"id": idx, "content": text, "type": "custom"})
        if self._built:
            all_docs = _build_knowledge_documents() + self._custom_docs
            self._store.build(all_docs)

    def chat(self, query: str, top_k: int = 5) -> str:
        """Answer a free-text question about ASPICE using RAG."""
        if not self._built:
            self.build_knowledge_base()
        retrieved = self._store.search(query, top_k=top_k)
        context = "\n\n---\n\n".join(d["content"] for d in retrieved)
        answer = _generate_response(query, context)
        self._history.append({"role": "user", "content": query})
        self._history.append({"role": "assistant", "content": answer})
        return answer

    def assess_process(self, process_id: str, pa_ratings: dict[str, str]) -> dict[str, Any]:
        """Assess a single process against PA ratings."""
        if not self._built:
            self.build_knowledge_base()
        result = assess_capability_level(pa_ratings)
        retrieved = self._store.search(f"{process_id} process outcomes work products", top_k=3)
        result["process_id"] = process_id
        result["process_context"] = "\n\n".join(d["content"] for d in retrieved)
        return result

    def assess_multiple_processes(self, assessments: dict[str, dict[str, str]]) -> dict[str, Any]:
        """Assess multiple processes at once."""
        results: dict[str, Any] = {}
        for proc_id, pa_ratings in assessments.items():
            results[proc_id] = self.assess_process(proc_id, pa_ratings)
        levels = [v["achieved_level"] for v in results.values()]
        summary = {
            "processes_assessed": len(results),
            "average_capability_level": round(sum(levels) / len(levels), 2) if levels else 0,
            "min_capability_level": min(levels) if levels else 0,
            "max_capability_level": max(levels) if levels else 0,
            "processes_at_level": {lvl: sum(1 for l in levels if l == lvl) for lvl in range(6)},
        }
        return {"results": results, "summary": summary}

    def get_process_info(self, process_id: str) -> dict[str, Any]:
        """Return structured information about a specific ASPICE process."""
        for group in PROCESS_GROUPS.values():
            if process_id in group["processes"]:
                return {"id": process_id, "group": group["name"], **group["processes"][process_id]}
        return {}

    def get_capability_level_info(self, level: int) -> dict[str, Any]:
        """Return structured information about a capability level."""
        return CAPABILITY_LEVELS.get(level, {})

    def get_assessment_questions(self, pa_id: str) -> list[str]:
        """Return assessment checklist questions for a process attribute."""
        return ASSESSMENT_QUESTIONS.get(pa_id, [])

    def get_all_processes(self) -> list[str]:
        """Return a sorted list of all ASPICE process IDs."""
        pids: list[str] = []
        for group in PROCESS_GROUPS.values():
            pids.extend(group["processes"].keys())
        return sorted(pids)

    def get_improvement_roadmap(
        self,
        current_assessments: dict[str, dict[str, str]],
        target_level: int,
    ) -> dict[str, Any]:
        """Generate an improvement roadmap to reach a target capability level."""
        roadmap: dict[str, Any] = {"target_level": target_level, "processes": {}}
        for proc_id, pa_ratings in current_assessments.items():
            result = assess_capability_level(pa_ratings)
            current = result["achieved_level"]
            if current >= target_level:
                roadmap["processes"][proc_id] = {
                    "status": "achieved", "current_level": current, "actions": []
                }
                continue
            actions: list[str] = []
            for lvl in range(current + 1, target_level + 1):
                rule = LEVEL_ACHIEVEMENT_RULES.get(lvl, {})
                for pa, allowed in rule.get("required_ratings", {}).items():
                    actual = pa_ratings.get(pa, "N")
                    if actual not in allowed:
                        questions = ASSESSMENT_QUESTIONS.get(pa, [])
                        actions.append(
                            f"Level {lvl} - Improve {pa} from '{actual}' to "
                            f"'{allowed[0]}': {questions[0] if questions else 'See standard.'}"
                        )
            roadmap["processes"][proc_id] = {
                "status": "gap",
                "current_level": current,
                "target_level": target_level,
                "actions": actions,
            }
        return roadmap

    def get_history(self) -> list[dict[str, str]]:
        """Return the conversation history."""
        return list(self._history)

    def clear_history(self) -> None:
        """Clear the conversation history."""
        self._history.clear()
