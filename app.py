"""
ASPICE Capability Checker — Streamlit application
=================================================
A RAG-powered agent for ASPICE v4.0 process capability assessment.
Run with:  streamlit run app.py
"""

from __future__ import annotations

import json
import os
import sys

import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, os.path.dirname(__file__))
from src.aspice_knowledge import (
    ASSESSMENT_QUESTIONS,
    CAPABILITY_LEVELS,
    PROCESS_GROUPS,
    RATING_SCALE,
)
from src.rag_engine import AspiceAgent

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="ASPICE Capability Checker",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------------------------

st.markdown(
    """
<style>
    .main-header {
        background: linear-gradient(135deg, #1a237e 0%, #283593 50%, #3949ab 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .main-header h1 { margin: 0; font-size: 2.2rem; }
    .main-header p  { margin: 0.4rem 0 0; opacity: 0.85; font-size: 1.05rem; }

    .capability-card {
        border-left: 6px solid #1a237e;
        padding: 1rem 1.2rem;
        border-radius: 0 8px 8px 0;
        margin: 0.5rem 0;
    }
    .level-0  { background: #ffebee; border-color: #b71c1c; }
    .level-1  { background: #fff3e0; border-color: #e65100; }
    .level-2  { background: #fff8e1; border-color: #f57f17; }
    .level-3  { background: #e8f5e9; border-color: #1b5e20; }
    .level-4  { background: #e3f2fd; border-color: #0d47a1; }
    .level-5  { background: #f3e5f5; border-color: #4a148c; }

    .metric-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        border: 1px solid #dee2e6;
    }
    .metric-card .value { font-size: 2rem; font-weight: bold; color: #1a237e; }
    .metric-card .label { font-size: 0.85rem; color: #6c757d; }

    .gap-item   { background: #fff3e0; border-left: 4px solid #ff6f00; padding: 0.6rem 0.9rem; border-radius: 0 6px 6px 0; margin: 0.3rem 0; }
    .rec-item   { background: #e8f5e9; border-left: 4px solid #2e7d32; padding: 0.6rem 0.9rem; border-radius: 0 6px 6px 0; margin: 0.3rem 0; }
    .chat-user  { background: #e3f2fd; padding: 0.8rem 1rem; border-radius: 12px 12px 12px 0; margin: 0.4rem 0; }
    .chat-agent { background: #f3e5f5; padding: 0.8rem 1rem; border-radius: 12px 12px 0 12px; margin: 0.4rem 0; }
    .stButton > button { border-radius: 8px; }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------


def _init_state() -> None:
    if "agent" not in st.session_state:
        st.session_state.agent = AspiceAgent()
        st.session_state.agent.build_knowledge_base()
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "pa_ratings" not in st.session_state:
        st.session_state.pa_ratings = {}
    if "multi_results" not in st.session_state:
        st.session_state.multi_results = None
    if "custom_knowledge_added" not in st.session_state:
        st.session_state.custom_knowledge_added = []


_init_state()

agent: AspiceAgent = st.session_state.agent

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

st.markdown(
    """
<div class="main-header">
    <h1>🔍 ASPICE Capability Checker</h1>
    <p>AI-powered RAG Agent for ASPICE v4.0 Process Capability Assessment</p>
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown("## 🧭 Navigation")
    page = st.radio(
        "Select Mode",
        [
            "💬 ASPICE Q&A Chat",
            "📊 Capability Assessment",
            "📋 Multi-Process Assessment",
            "🗺️ Improvement Roadmap",
            "📚 ASPICE Knowledge Base",
            "🧠 Knowledge Enhancement",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("### ⚙️ Configuration")
    api_key = st.text_input(
        "OpenAI API Key (optional)",
        type="password",
        placeholder="sk-...",
        help="Leave blank to use the built-in rule-based engine.",
    )
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        st.success("✅ OpenAI key set — using GPT-4o")
    else:
        st.info("ℹ️ No API key — using built-in engine")

    st.markdown("---")
    st.markdown(
        """
**ASPICE v4.0 Capability Levels**
| Level | Name        |
|-------|-------------|
| 0     | Incomplete  |
| 1     | Performed   |
| 2     | Managed     |
| 3     | Established |
| 4     | Predictable |
| 5     | Optimizing  |
"""
    )


# ---------------------------------------------------------------------------
# Helper: gauge chart
# ---------------------------------------------------------------------------


def _gauge(level: int, title: str = "Capability Level") -> go.Figure:
    colours = ["#b71c1c", "#e65100", "#f57f17", "#1b5e20", "#0d47a1", "#4a148c"]
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=level,
            title={"text": title, "font": {"size": 16}},
            delta={"reference": 3, "increasing": {"color": "#2e7d32"}, "decreasing": {"color": "#b71c1c"}},
            gauge={
                "axis": {"range": [0, 5], "tickwidth": 1, "tickvals": list(range(6))},
                "bar": {"color": colours[level]},
                "steps": [
                    {"range": [0, 1], "color": "#ffebee"},
                    {"range": [1, 2], "color": "#fff3e0"},
                    {"range": [2, 3], "color": "#fff8e1"},
                    {"range": [3, 4], "color": "#e8f5e9"},
                    {"range": [4, 5], "color": "#e3f2fd"},
                ],
                "threshold": {"line": {"color": "#4a148c", "width": 4}, "thickness": 0.75, "value": 3},
            },
        )
    )
    fig.update_layout(height=280, margin=dict(t=40, b=20, l=20, r=20))
    return fig


# ===========================================================================
# PAGE: ASPICE Q&A Chat
# ===========================================================================

if page == "💬 ASPICE Q&A Chat":
    st.markdown("## 💬 ASPICE Knowledge Q&A")
    st.markdown(
        "Ask any question about ASPICE v4.0 — capability levels, processes, work products, "
        "base practices, and more."
    )

    # Quick-start buttons
    st.markdown("**Quick questions:**")
    cols = st.columns(3)
    quick_qs = [
        "What is ASPICE Level 2?",
        "What are SWE.1 base practices?",
        "How is PA 3.1 assessed?",
        "What work products does SUP.8 require?",
        "Explain the difference between Level 3 and Level 4",
        "What is the rating scale in ASPICE?",
    ]
    for i, q in enumerate(quick_qs):
        if cols[i % 3].button(q, key=f"quick_{i}"):
            st.session_state.chat_history.append({"role": "user", "content": q})
            with st.spinner("Searching ASPICE knowledge base…"):
                answer = agent.chat(q)
            st.session_state.chat_history.append({"role": "assistant", "content": answer})

    # Chat display
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-user">👤 **You:** {msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-agent">🤖 **ASPICE Agent:**\n\n{msg["content"]}</div>', unsafe_allow_html=True)

    # Input
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_area("Your question:", height=80, placeholder="Ask about ASPICE v4.0…")
        submitted = st.form_submit_button("Send 📨", use_container_width=True)

    if submitted and user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("Searching ASPICE knowledge base…"):
            answer = agent.chat(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        st.rerun()

    if st.button("🗑️ Clear conversation"):
        st.session_state.chat_history.clear()
        agent.clear_history()
        st.rerun()


# ===========================================================================
# PAGE: Single-Process Capability Assessment
# ===========================================================================

elif page == "📊 Capability Assessment":
    st.markdown("## 📊 Single Process Capability Assessment")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Process Selection")
        all_procs = agent.get_all_processes()
        process_id = st.selectbox("Select ASPICE Process", all_procs)

        proc_info = agent.get_process_info(process_id)
        if proc_info:
            st.info(f"**{proc_info['name']}**\n\n{proc_info['purpose'][:300]}…")

        st.markdown("### Rate Process Attributes")
        st.caption("Rate each applicable Process Attribute (PA) using N/P/L/F")

        target_level = st.slider("Target Capability Level", 1, 5, 3)

        pa_options = ["N", "P", "L", "F"]
        pa_labels = {k: f"{k} — {v['name']} ({v['range']})" for k, v in RATING_SCALE.items()}

        pa_ratings: dict[str, str] = {}

        # Show PAs up to target+1 for context
        all_pas = [
            "PA 1.1",
            "PA 2.1", "PA 2.2",
            "PA 3.1", "PA 3.2",
            "PA 4.1", "PA 4.2",
            "PA 5.1", "PA 5.2",
        ]
        for pa in all_pas:
            pa_ratings[pa] = st.selectbox(
                pa,
                pa_options,
                format_func=lambda x: pa_labels[x],
                key=f"pa_{pa}",
            )

        assess_btn = st.button("🔍 Assess Capability", use_container_width=True, type="primary")

    with col2:
        if assess_btn or st.session_state.pa_ratings:
            if assess_btn:
                st.session_state.pa_ratings = pa_ratings

            result = agent.assess_process(process_id, st.session_state.pa_ratings)

            # Gauge
            st.plotly_chart(_gauge(result["achieved_level"]), use_container_width=True)

            level_class = f"level-{result['achieved_level']}"
            st.markdown(
                f'<div class="capability-card {level_class}">'
                f"<strong>Process:</strong> {result['process_id']} — "
                f"<strong>Achieved Level:</strong> {result['achieved_level']} "
                f"({result['level_name']})<br>"
                f"<em>{result['level_description'][:200]}…</em>"
                f"</div>",
                unsafe_allow_html=True,
            )

            # PA details table
            st.markdown("### Process Attribute Ratings")
            pa_rows = []
            for pa in result["pa_details"]:
                colour = {"F": "🟢", "L": "🟡", "P": "🟠", "N": "🔴"}.get(pa["rating"], "⚪")
                pa_rows.append(
                    {
                        "PA": pa["pa"],
                        "Rating": f"{colour} {pa['rating']} — {pa['rating_name']}",
                        "Range": pa["range"],
                    }
                )
            st.table(pa_rows)

            # Gaps
            if result["gaps"]:
                st.markdown("### ⚠️ Identified Gaps")
                for gap in result["gaps"]:
                    st.markdown(f'<div class="gap-item">⚠️ {gap}</div>', unsafe_allow_html=True)

            # Recommendations
            if result["recommendations"]:
                st.markdown("### 💡 Recommendations")
                for rec in result["recommendations"]:
                    st.markdown(f'<div class="rec-item">✅ {rec}</div>', unsafe_allow_html=True)

            # Assessment questions for each PA
            with st.expander("📋 Assessment Checklist Questions"):
                for pa, rating in st.session_state.pa_ratings.items():
                    questions = agent.get_assessment_questions(pa)
                    if questions:
                        st.markdown(f"**{pa}** (currently: {rating})")
                        for q in questions:
                            st.markdown(f"  - {q}")


# ===========================================================================
# PAGE: Multi-Process Assessment
# ===========================================================================

elif page == "📋 Multi-Process Assessment":
    st.markdown("## 📋 Multi-Process Capability Assessment")
    st.markdown(
        "Assess multiple ASPICE processes simultaneously and compare their capability levels."
    )

    tab1, tab2 = st.tabs(["⌨️ Manual Input", "📄 JSON Import"])

    with tab1:
        all_procs = agent.get_all_processes()
        selected_procs = st.multiselect(
            "Select Processes to Assess",
            all_procs,
            default=["SWE.1", "SWE.2", "MAN.3", "SUP.1", "SUP.8"],
        )

        if selected_procs:
            multi_ratings: dict[str, dict[str, str]] = {}
            pa_list = ["PA 1.1", "PA 2.1", "PA 2.2", "PA 3.1", "PA 3.2"]

            for proc in selected_procs:
                with st.expander(f"🔧 {proc} — Rate Process Attributes"):
                    proc_ratings: dict[str, str] = {}
                    cols = st.columns(len(pa_list))
                    for i, pa in enumerate(pa_list):
                        proc_ratings[pa] = cols[i].selectbox(
                            pa, ["N", "P", "L", "F"], key=f"multi_{proc}_{pa}"
                        )
                    multi_ratings[proc] = proc_ratings

            if st.button("🔍 Assess All Processes", type="primary", use_container_width=True):
                with st.spinner("Assessing processes…"):
                    st.session_state.multi_results = agent.assess_multiple_processes(multi_ratings)

    with tab2:
        st.markdown(
            "Paste a JSON object mapping process IDs to PA ratings, e.g.:\n"
            "```json\n"
            '{"SWE.1": {"PA 1.1": "F", "PA 2.1": "L"}, "MAN.3": {"PA 1.1": "F"}}\n'
            "```"
        )
        json_input = st.text_area("JSON Input", height=200)
        if st.button("📥 Import & Assess", use_container_width=True):
            try:
                imported = json.loads(json_input)
                with st.spinner("Assessing processes…"):
                    st.session_state.multi_results = agent.assess_multiple_processes(imported)
                st.success("Assessment complete!")
            except json.JSONDecodeError as exc:
                st.error(f"Invalid JSON: {exc}")

    # Results
    if st.session_state.multi_results:
        results = st.session_state.multi_results
        summary = results["summary"]

        st.markdown("### 📈 Summary")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Processes Assessed", summary["processes_assessed"])
        c2.metric("Average Level", f"{summary['average_capability_level']:.1f}")
        c3.metric("Min Level", summary["min_capability_level"])
        c4.metric("Max Level", summary["max_capability_level"])

        # Bar chart
        procs_r = list(results["results"].keys())
        levels_r = [results["results"][p]["achieved_level"] for p in procs_r]
        colours_r = ["#b71c1c", "#e65100", "#f57f17", "#1b5e20", "#0d47a1", "#4a148c"]
        bar_colours = [colours_r[l] for l in levels_r]

        fig = go.Figure(
            go.Bar(
                x=procs_r,
                y=levels_r,
                marker_color=bar_colours,
                text=levels_r,
                textposition="auto",
            )
        )
        fig.update_layout(
            title="Capability Levels by Process",
            xaxis_title="Process",
            yaxis_title="Capability Level",
            yaxis=dict(range=[0, 5.5], tickvals=list(range(6))),
            height=380,
        )
        st.plotly_chart(fig, use_container_width=True)

        # Radar chart (if ≤ 12 processes)
        if len(procs_r) <= 12:
            fig2 = go.Figure(
                go.Scatterpolar(
                    r=levels_r + [levels_r[0]],
                    theta=procs_r + [procs_r[0]],
                    fill="toself",
                    line_color="#1a237e",
                )
            )
            fig2.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                title="Capability Radar",
                height=420,
            )
            st.plotly_chart(fig2, use_container_width=True)

        # Per-process details
        st.markdown("### 🔎 Per-Process Details")
        for proc_id, proc_result in results["results"].items():
            with st.expander(
                f"{proc_id} — Level {proc_result['achieved_level']} ({proc_result['level_name']})"
            ):
                if proc_result["gaps"]:
                    st.markdown("**Gaps:**")
                    for g in proc_result["gaps"]:
                        st.markdown(f"  ⚠️ {g}")
                if proc_result["recommendations"]:
                    st.markdown("**Recommendations:**")
                    for r in proc_result["recommendations"]:
                        st.markdown(f"  ✅ {r}")


# ===========================================================================
# PAGE: Improvement Roadmap
# ===========================================================================

elif page == "🗺️ Improvement Roadmap":
    st.markdown("## 🗺️ ASPICE Improvement Roadmap")
    st.markdown(
        "Define your current state and target capability level to generate an improvement roadmap."
    )

    col1, col2 = st.columns([1, 2])

    with col1:
        target = st.slider("Target Capability Level", 1, 5, 3)
        all_procs = agent.get_all_processes()
        selected = st.multiselect(
            "Processes in Scope",
            all_procs,
            default=["SWE.1", "SWE.2", "MAN.3", "SUP.1"],
        )

        current_state: dict[str, dict[str, str]] = {}
        for proc in selected:
            with st.expander(f"{proc} — Current PA Ratings"):
                ratings: dict[str, str] = {}
                for pa in ["PA 1.1", "PA 2.1", "PA 2.2", "PA 3.1", "PA 3.2"]:
                    ratings[pa] = st.selectbox(
                        pa, ["N", "P", "L", "F"], key=f"rm_{proc}_{pa}"
                    )
                current_state[proc] = ratings

        gen_btn = st.button("🗺️ Generate Roadmap", type="primary", use_container_width=True)

    with col2:
        if gen_btn and current_state:
            with st.spinner("Building improvement roadmap…"):
                roadmap = agent.get_improvement_roadmap(current_state, target)

            st.markdown(f"### 🎯 Target: Capability Level {target}")

            for proc_id, proc_plan in roadmap["processes"].items():
                status_icon = "✅" if proc_plan["status"] == "achieved" else "🔧"
                with st.expander(
                    f"{status_icon} {proc_id} — Current Level {proc_plan['current_level']}"
                ):
                    if proc_plan["status"] == "achieved":
                        st.success(f"Target level {target} already achieved!")
                    else:
                        st.warning(
                            f"Gap: Current Level {proc_plan['current_level']} → "
                            f"Target Level {proc_plan['target_level']}"
                        )
                        st.markdown("**Required Actions:**")
                        for i, action in enumerate(proc_plan["actions"], 1):
                            st.markdown(f"  {i}. {action}")


# ===========================================================================
# PAGE: ASPICE Knowledge Base
# ===========================================================================

elif page == "📚 ASPICE Knowledge Base":
    st.markdown("## 📚 ASPICE v4.0 Knowledge Base")

    kb_tab1, kb_tab2, kb_tab3 = st.tabs(
        ["🏗️ Processes", "📏 Capability Levels", "❓ Assessment Questions"]
    )

    with kb_tab1:
        group_filter = st.selectbox(
            "Filter by Process Group",
            ["All"] + list(PROCESS_GROUPS.keys()),
        )
        for group_id, group in PROCESS_GROUPS.items():
            if group_filter not in ("All", group_id):
                continue
            st.markdown(f"### {group_id} — {group['name']}")
            for proc_id, proc in group["processes"].items():
                with st.expander(f"**{proc_id}** — {proc['name']}"):
                    st.markdown(f"**Purpose:** {proc['purpose']}")
                    st.markdown("**Outcomes:**")
                    for o in proc["outcomes"]:
                        st.markdown(f"  - {o}")
                    st.markdown("**Work Products:**")
                    for w in proc["work_products"]:
                        st.markdown(f"  - {w}")
                    st.markdown("**Base Practices:**")
                    for b in proc["base_practices"]:
                        st.markdown(f"  - {b}")

    with kb_tab2:
        for level, data in CAPABILITY_LEVELS.items():
            level_class = f"level-{level}"
            st.markdown(
                f'<div class="capability-card {level_class}">'
                f"<strong>Level {level}: {data['name']}</strong><br>"
                f"{data['description']}"
                f"</div>",
                unsafe_allow_html=True,
            )
            for pa in data.get("process_attributes", []):
                with st.expander(f"  {pa['id']} — {pa['name']}"):
                    st.markdown(f"**Description:** {pa['description']}")
                    st.markdown("**Indicators:**")
                    for ind in pa["indicators"]:
                        st.markdown(f"  - {ind}")

    with kb_tab3:
        pa_sel = st.selectbox("Select Process Attribute", list(ASSESSMENT_QUESTIONS.keys()))
        questions = ASSESSMENT_QUESTIONS.get(pa_sel, [])
        st.markdown(f"### Assessment Questions for {pa_sel}")
        for i, q in enumerate(questions, 1):
            st.markdown(f"**{i}.** {q}")


# ===========================================================================
# PAGE: Knowledge Enhancement
# ===========================================================================

elif page == "🧠 Knowledge Enhancement":
    st.markdown("## 🧠 Knowledge Enhancement")
    st.markdown(
        "Enhance the ASPICE agent with organisation-specific knowledge — process descriptions, "
        "lessons learned, templates, or custom checklists."
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### ➕ Add Custom Knowledge")
        doc_title = st.text_input("Document Title / ID", placeholder="e.g. OrgProcess_SWE1_Tailoring")
        custom_text = st.text_area(
            "Knowledge Content",
            height=250,
            placeholder=(
                "Paste your organisation's process description, lessons learned, "
                "tailoring guidelines, or any ASPICE-related content here…"
            ),
        )
        if st.button("📥 Add to Knowledge Base", type="primary", use_container_width=True):
            if custom_text.strip():
                agent.add_custom_knowledge(custom_text, doc_id=doc_title or None)
                st.session_state.custom_knowledge_added.append(
                    {"id": doc_title or f"DOC_{len(st.session_state.custom_knowledge_added)}", "preview": custom_text[:120] + "…"}
                )
                st.success("✅ Knowledge added and index updated!")
            else:
                st.warning("Please enter some content.")

        # Pre-built templates
        st.markdown("### 📝 Quick Templates")
        template = st.selectbox(
            "Load a template",
            [
                "— Select —",
                "SWE.1 Tailoring Guideline",
                "Functional Safety (ISO 26262) Overlay",
                "Agile-ASPICE Bridge Notes",
                "Supplier Assessment Checklist",
            ],
        )
        templates = {
            "SWE.1 Tailoring Guideline": (
                "SWE.1 Tailoring for Embedded Projects:\n"
                "- Requirement IDs must follow REQ-<module>-<seq> format.\n"
                "- DOORS NG is the approved tool for requirements management.\n"
                "- Software requirements must be reviewed by both SW lead and system architect.\n"
                "- Traceability to system requirements is mandatory for all Level 2+ projects.\n"
                "- Acceptance criteria must include measurable performance criteria."
            ),
            "Functional Safety (ISO 26262) Overlay": (
                "ISO 26262 / ASPICE Integration Notes:\n"
                "- ASPICE SWE.1 maps to ISO 26262 Part 6 clause 7 (software safety requirements).\n"
                "- For ASIL C/D items, all SWE processes must be at minimum Level 2.\n"
                "- Safety cases must reference ASPICE work products.\n"
                "- SUP.1 (QA) audits must cover safety-relevant processes with increased frequency.\n"
                "- MAN.5 risk register must include safety risk items."
            ),
            "Agile-ASPICE Bridge Notes": (
                "Agile Methodology mapped to ASPICE:\n"
                "- Sprint planning corresponds to MAN.3 activity planning.\n"
                "- User stories serve as inputs to SWE.1 (requirements analysis).\n"
                "- Definition of Done must satisfy SWE.4/SWE.5 exit criteria.\n"
                "- Sprint retrospectives satisfy MAN.3 monitoring and corrective action.\n"
                "- Backlog grooming contributes to SUP.10 (change request management).\n"
                "- CI/CD pipeline outputs serve as SWE.5 integration test evidence."
            ),
            "Supplier Assessment Checklist": (
                "Supplier ASPICE Assessment Checklist:\n"
                "- Verify supplier has documented processes for all contracted process areas.\n"
                "- Check evidence of Level 2 achievement for SWE.1, SWE.2, SWE.3 at minimum.\n"
                "- Review PA 2.2 work product management records for completeness.\n"
                "- Confirm traceability records exist from requirements to test results.\n"
                "- Validate configuration management plan and change history are maintained.\n"
                "- Review problem/defect tracking system and trend analysis reports."
            ),
        }
        if template != "— Select —" and st.button("📋 Load Template"):
            st.session_state["template_text"] = templates[template]
            st.rerun()

        if "template_text" in st.session_state:
            st.text_area("Template Content (copy & edit above)", value=st.session_state["template_text"], height=180)

    with col2:
        st.markdown("### 📂 Added Custom Knowledge")
        if st.session_state.custom_knowledge_added:
            for doc in st.session_state.custom_knowledge_added:
                st.markdown(
                    f"**{doc['id']}**\n> {doc['preview']}",
                )
        else:
            st.info("No custom knowledge added yet.")

        st.markdown("---")
        st.markdown("### 🔍 Test Enhanced Knowledge")
        test_q = st.text_input("Ask a question using your custom knowledge:")
        if st.button("Ask Agent 🤖") and test_q:
            with st.spinner("Querying enhanced knowledge base…"):
                answer = agent.chat(test_q)
            st.markdown("**Answer:**")
            st.markdown(answer)

        st.markdown("---")
        st.markdown("### 📊 Knowledge Base Statistics")
        all_procs = agent.get_all_processes()
        total_processes = len(all_procs)
        total_custom = len(st.session_state.custom_knowledge_added)
        st.metric("ASPICE v4.0 Processes", total_processes)
        st.metric("Capability Levels", 6)
        st.metric("Custom Documents Added", total_custom)
        st.metric(
            "Total Knowledge Chunks",
            total_processes + 6 + len(ASSESSMENT_QUESTIONS) + 2 + total_custom,
        )


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:#6c757d;font-size:0.85rem;'>"
    "ASPICE Capability Checker &nbsp;|&nbsp; Based on ASPICE v4.0 / ISO/IEC 33020 "
    "&nbsp;|&nbsp; RAG-powered by sentence-transformers + FAISS"
    "</div>",
    unsafe_allow_html=True,
)
