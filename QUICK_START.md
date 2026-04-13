# ASPICE Capability Checker - Quick Start Guide

Get up and running with the ASPICE Capability Checker in 5 minutes!

---

## Installation (2 minutes)

```bash
# 1. Navigate to the project directory
cd ASPICE-Capability-Checker

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Set up OpenAI API key
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=sk-your-key-here
```

---

## Launch the Application (1 minute)

### Web Interface (Recommended)
```bash
streamlit run app.py
```
The app opens automatically at `http://localhost:8501`

### Command-Line Interface
```bash
python cli.py chat
```

---

## Try These Features (2 minutes)

### 1. Ask a Question
1. Go to **💬 ASPICE Q&A Chat** page
2. Click "What is ASPICE Level 2?" or type your own question
3. Get instant answers from ASPICE v4.0 knowledge base

### 2. Assess a Process
1. Navigate to **📊 Capability Assessment**
2. Select a process (e.g., "SWE.1")
3. Rate Process Attributes:
   - PA 1.1: F (Fully achieved)
   - PA 2.1: F
   - PA 2.2: F
4. Click **🔍 Assess Capability**
5. View achieved level, gaps, and recommendations

### 3. Generate Improvement Roadmap
1. Go to **🗺️ Improvement Roadmap**
2. Set target level (e.g., 3)
3. Select processes (e.g., SWE.1, MAN.3)
4. Rate current state for each
5. Click **🗺️ Generate Roadmap**
6. See step-by-step improvement actions

---

## Common Use Cases

### For Quality Managers
**Goal**: Prepare for upcoming ASPICE assessment

**Quick Path**:
1. **Multi-Process Assessment** → Select all in-scope processes
2. Rate current PA achievement for each
3. Review summary metrics and identify weakest areas
4. **Improvement Roadmap** → Generate plan to address gaps
5. **Knowledge Base** → Review assessment questions for verification

---

### For Developers
**Goal**: Understand what my process requires

**Quick Path**:
1. **ASPICE Knowledge Base** → Select your process (e.g., SWE.1)
2. Review outcomes, work products, and base practices
3. **Q&A Chat** → Ask specific questions like "What work products does SWE.1 require?"
4. **Assessment Questions** tab → Review checklist questions

---

### For Process Engineers
**Goal**: Improve process capability

**Quick Path**:
1. **Capability Assessment** → Assess current level
2. Review gaps and recommendations
3. **Improvement Roadmap** → Get detailed action plan
4. **Knowledge Enhancement** → Add organization-specific guidelines
5. Reassess periodically to track improvement

---

## CLI Quick Commands

```bash
# Interactive Q&A
python cli.py chat

# Assess a process
python cli.py assess --process SWE.1

# Assess with pre-defined ratings
python cli.py assess --process SWE.1 --ratings '{"PA 1.1":"F","PA 2.1":"F","PA 2.2":"F"}'

# Generate improvement roadmap
python cli.py roadmap --target 3 --processes SWE.1 SWE.2 MAN.3

# View capability levels
python cli.py levels

# Get process details
python cli.py info --process MAN.3
```

---

## Programmatic Usage

```python
from src.rag_engine import AspiceAgent

# Initialize
agent = AspiceAgent()
agent.build_knowledge_base()

# Ask questions
answer = agent.chat("What is ASPICE Level 2?")
print(answer)

# Assess a process
result = agent.assess_process(
    "SWE.1",
    {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"}
)
print(f"Level: {result['achieved_level']} - {result['level_name']}")

# Multi-process assessment
results = agent.assess_multiple_processes({
    "SWE.1": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"},
    "MAN.3": {"PA 1.1": "F"},
})
print(f"Average Level: {results['summary']['average_capability_level']}")

# Generate roadmap
roadmap = agent.get_improvement_roadmap(
    {"SWE.1": {"PA 1.1": "F", "PA 2.1": "N"}},
    target_level=3
)

# Add custom knowledge
agent.add_custom_knowledge(
    "Our company uses DOORS NG for requirements management.",
    doc_id="ORG_PROCESS_SWE1"
)
```

---

## Understanding the Output

### Capability Levels
- **Level 0**: Incomplete - Process fails to achieve purpose
- **Level 1**: Performed - Process achieves its purpose
- **Level 2**: Managed - Process is planned, monitored, controlled
- **Level 3**: Established - Uses defined standard process
- **Level 4**: Predictable - Operates within quantitative limits
- **Level 5**: Optimizing - Continuously improved

### Rating Scale
- **N**: Not achieved (0-15%)
- **P**: Partially achieved (15-50%)
- **L**: Largely achieved (50-85%)
- **F**: Fully achieved (85-100%)

### Capability Level Requirements
- **Level 1**: PA 1.1 = L or F
- **Level 2**: PA 1.1, 2.1, 2.2 = F (or one L)
- **Level 3**: All Level 2 PAs = F, plus PA 3.1, 3.2 = F

---

## Tips for Success

### ✅ Do's
- ✅ Start with Q&A Chat to learn ASPICE concepts
- ✅ Be conservative with ratings (when in doubt, rate lower)
- ✅ Use Assessment Questions to verify your ratings
- ✅ Review recommendations and implement systematically
- ✅ Add custom knowledge for organization-specific processes
- ✅ Reassess regularly to track progress

### ❌ Don'ts
- ❌ Don't rate "Fully achieved" without comprehensive evidence
- ❌ Don't skip lower levels (they're cumulative)
- ❌ Don't try to jump from Level 1 to Level 3
- ❌ Don't ignore gaps - address them systematically
- ❌ Don't assess processes not in scope

---

## Need More Help?

📘 **[Complete User Manual](USER_MANUAL.md)** - Comprehensive guide with 40+ detailed use cases

### Key Manual Sections
- [Installation Guide](USER_MANUAL.md#getting-started)
- [Detailed Use Cases](USER_MANUAL.md#features-and-use-cases)
- [Understanding ASPICE](USER_MANUAL.md#understanding-aspice)
- [Troubleshooting](USER_MANUAL.md#troubleshooting)
- [Best Practices](USER_MANUAL.md#best-practices)
- [FAQ](USER_MANUAL.md#faq)

---

## Common Issues

**Issue**: Streamlit won't start
```bash
# Solution: Try a different port
streamlit run app.py --server.port 8502
```

**Issue**: "Invalid JSON" in multi-process assessment
```json
// Use double quotes, not single quotes
{"SWE.1": {"PA 1.1": "F"}}  // ✅ Correct
{'SWE.1': {'PA 1.1': 'F'}}  // ❌ Wrong
```

**Issue**: OpenAI API not working
```bash
# Solution: Works without API key using built-in engine
# Just leave the API key field blank
```

---

## Next Steps

1. **Learn**: Explore Q&A Chat and Knowledge Base
2. **Assess**: Evaluate your current processes
3. **Improve**: Follow roadmap recommendations
4. **Customize**: Add organization-specific knowledge
5. **Automate**: Integrate via CLI or API

---

**Ready to dive deeper?** → [Read the Full User Manual](USER_MANUAL.md)

**Quick questions?** → Launch the app and use **💬 ASPICE Q&A Chat**
