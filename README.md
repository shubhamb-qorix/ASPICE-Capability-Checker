# ASPICE Capability Checker

An AI-powered **RAG (Retrieval-Augmented Generation) agent** for assessing and verifying ASPICE v4.0 process capability levels. The agent combines an embedded ASPICE v4.0 knowledge base with semantic search and optional LLM generation to provide accurate, standards-compliant assessment guidance.

📘 **[Read the Complete User Manual](USER_MANUAL.md)** — Detailed guide with 40+ use cases for all features

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **RAG Pipeline** | FAISS vector store + sentence-transformers for semantic retrieval over ASPICE v4.0 |
| 📊 **Capability Level Assessment** | Verifies PA ratings against ISO/IEC 33020 rules (Levels 0–5) |
| 📋 **Multi-Process Assessment** | Assess multiple ASPICE processes simultaneously with summary charts |
| 🗺️ **Improvement Roadmap** | Gap analysis and action plans to reach a target capability level |
| 💬 **Q&A Chat** | Natural-language questions answered from ASPICE v4.0 knowledge |
| 🧠 **Knowledge Enhancement** | Add organisation-specific knowledge (tailoring guidelines, lessons learned) |
| 🌐 **Streamlit UI** | Interactive web interface with gauges, radar charts, and checklists |
| ⌨️ **CLI** | Full command-line interface for scripted workflows |
| 🤖 **OpenAI GPT-4o (optional)** | Set `OPENAI_API_KEY` to upgrade to AI-generated responses |

---

## 🏗️ Architecture

```
ASPICE Capability Checker
├── app.py                      # Streamlit web UI
├── cli.py                      # Command-line interface
├── requirements.txt
├── .env.example
├── src/
│   ├── __init__.py
│   ├── aspice_knowledge.py     # ASPICE v4.0 knowledge base (processes, PAs, questions)
│   └── rag_engine.py           # RAG pipeline, vector store, assessment engine
└── tests/
    └── test_aspice_agent.py    # Pytest test suite
```

### RAG Pipeline

```
User Query
    │
    ▼
Sentence-Transformer Encoder (all-MiniLM-L6-v2)
    │
    ▼
FAISS Index (cosine similarity search)
    │
    ▼
Top-K Retrieved ASPICE Chunks
    │
    ├── (no API key) → Rule-based response with retrieved context
    └── (OPENAI_API_KEY set) → GPT-4o generation with context
    │
    ▼
Structured Answer
```

---

## 📐 ASPICE v4.0 Coverage

### Capability Levels (ISO/IEC 33020)

| Level | Name | Key Process Attributes |
|---|---|---|
| 0 | Incomplete | — |
| 1 | Performed | PA 1.1 Process Performance |
| 2 | Managed | PA 2.1 Performance Mgmt, PA 2.2 Work Product Mgmt |
| 3 | Established | PA 3.1 Process Definition, PA 3.2 Process Deployment |
| 4 | Predictable | PA 4.1 Quantitative Analysis, PA 4.2 Quantitative Control |
| 5 | Optimizing | PA 5.1 Process Innovation, PA 5.2 Process Optimization |

### Process Areas Covered

| Group | Processes |
|---|---|
| **SWE** Software Engineering | SWE.1 – SWE.6 |
| **SYS** System Engineering | SYS.1 – SYS.5 |
| **MAN** Management | MAN.3, MAN.5, MAN.6 |
| **SUP** Support | SUP.1, SUP.8, SUP.9, SUP.10 |
| **ACQ** Acquisition | ACQ.4 |

### Rating Scale (ISO/IEC 33020)

| Code | Name | Achievement |
|---|---|---|
| N | Not achieved | 0–15% |
| P | Partially achieved | 15–50% |
| L | Largely achieved | 50–85% |
| F | Fully achieved | 85–100% |

---

## 🚀 Quick Start

🚀 **[Quick Start Guide](QUICK_START.md)** — Get running in 5 minutes!

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. (Optional) Configure OpenAI

```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 3. Launch the web UI

```bash
streamlit run app.py
```

### 4. Or use the CLI

```bash
# Interactive Q&A
python cli.py chat

# Assess a single process (interactive PA rating input)
python cli.py assess --process SWE.1

# Assess with pre-defined ratings (JSON)
python cli.py assess --process SWE.1 --ratings '{"PA 1.1":"F","PA 2.1":"L","PA 2.2":"F"}'

# Show all capability levels
python cli.py levels

# Show process details
python cli.py info --process MAN.3

# Generate improvement roadmap
python cli.py roadmap --target 3 --processes SWE.1 SWE.2 MAN.3
```

---

## 🧪 Running Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

---

## 💻 Programmatic API

```python
from src.rag_engine import AspiceAgent

# Initialise and build knowledge base
agent = AspiceAgent()
agent.build_knowledge_base()

# 1. Natural-language Q&A
answer = agent.chat("What work products does SWE.1 require?")

# 2. Single-process capability assessment
result = agent.assess_process(
    "SWE.1",
    {"PA 1.1": "F", "PA 2.1": "L", "PA 2.2": "F"}
)
print(f"Achieved Level: {result['achieved_level']} — {result['level_name']}")

# 3. Multi-process assessment
results = agent.assess_multiple_processes({
    "SWE.1": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"},
    "MAN.3": {"PA 1.1": "F"},
})

# 4. Improvement roadmap
roadmap = agent.get_improvement_roadmap(
    {"SWE.1": {"PA 1.1": "F", "PA 2.1": "N"}},
    target_level=3
)

# 5. Add organisation-specific knowledge
agent.add_custom_knowledge(
    "Our SWE.1 process uses DOORS NG for requirements management.",
    doc_id="ORG_SWE1_PROCESS"
)
```

---

## 🧠 Knowledge Enhancement

The agent supports runtime knowledge enhancement — add your organisation's:

- **Process tailoring guidelines**
- **Lessons learned** from previous ASPICE assessments
- **Tool-specific guidance** (e.g. DOORS, Jira, Git)
- **Functional Safety (ISO 26262) overlays**
- **Agile-ASPICE bridge notes**
- **Supplier assessment checklists**

---

## 🌐 Streamlit UI Pages

| Page | Description |
|---|---|
| 💬 ASPICE Q&A Chat | Ask any ASPICE question via chat interface |
| 📊 Capability Assessment | Assess a single process with gauge visualisation |
| 📋 Multi-Process Assessment | Compare multiple processes with bar/radar charts |
| 🗺️ Improvement Roadmap | Gap analysis with step-by-step action plans |
| 📚 ASPICE Knowledge Base | Browse all ASPICE v4.0 processes, levels, and questions |
| 🧠 Knowledge Enhancement | Add custom knowledge and test the enhanced agent |

---

## 🔒 Security & Privacy

- No data is sent externally unless `OPENAI_API_KEY` is set.
- With no API key the agent runs fully locally using sentence-transformers and FAISS.

---

## 📚 Documentation

### User Manual
The comprehensive **[USER_MANUAL.md](USER_MANUAL.md)** includes:
- **8 major feature sections** with detailed explanations
- **40+ real-world use cases** with step-by-step instructions
- **Understanding ASPICE** — Capability levels, rating scales, and process areas
- **Troubleshooting guide** — Solutions to common issues
- **Best practices** — Tips for effective assessment and improvement
- **FAQ** — Frequently asked questions

### Quick Links
- [Getting Started Guide](USER_MANUAL.md#getting-started)
- [Feature Use Cases](USER_MANUAL.md#features-and-use-cases)
- [CLI Commands](USER_MANUAL.md#7-command-line-interface-cli)
- [Programmatic API Examples](USER_MANUAL.md#8-programmatic-api)
- [Troubleshooting](USER_MANUAL.md#troubleshooting)

---

## 📖 Standards References

- **Automotive SPICE® v4.0** — Process Assessment Model (PAM)
- **ISO/IEC 33020** — Process measurement framework for assessment
- **ISO/IEC 33001** — Concepts and terminology for process assessment

---

## 📄 License

MIT License
