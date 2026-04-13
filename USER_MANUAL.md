# ASPICE Capability Checker - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Features and Use Cases](#features-and-use-cases)
   - [1. ASPICE Q&A Chat](#1-aspice-qa-chat)
   - [2. Single Process Capability Assessment](#2-single-process-capability-assessment)
   - [3. Multi-Process Assessment](#3-multi-process-assessment)
   - [4. Improvement Roadmap](#4-improvement-roadmap)
   - [5. ASPICE Knowledge Base Browser](#5-aspice-knowledge-base-browser)
   - [6. Knowledge Enhancement](#6-knowledge-enhancement)
   - [7. Command-Line Interface (CLI)](#7-command-line-interface-cli)
   - [8. Programmatic API](#8-programmatic-api)
4. [Understanding ASPICE](#understanding-aspice)
5. [Troubleshooting](#troubleshooting)
6. [Best Practices](#best-practices)
7. [FAQ](#faq)

---

## Introduction

The **ASPICE Capability Checker** is an AI-powered RAG (Retrieval-Augmented Generation) agent designed to help automotive software teams assess and improve their ASPICE v4.0 process capability levels. The tool combines semantic search over an embedded ASPICE v4.0 knowledge base with optional LLM generation to provide accurate, standards-compliant assessment guidance.

### Key Benefits
- **Objective Assessment**: Rule-based capability level verification following ISO/IEC 33020
- **Time-Saving**: Automated analysis and recommendations reduce assessment preparation time
- **Knowledge Access**: Instant answers to ASPICE questions without manual document searches
- **Improvement Planning**: Gap analysis and actionable roadmaps for capability improvements
- **Customizable**: Enhance with organization-specific knowledge and tailoring guidelines

### Who Should Use This Tool?
- **Quality Managers**: Planning and executing ASPICE assessments
- **Process Engineers**: Improving process capability maturity
- **Project Managers**: Understanding process requirements for projects
- **Software Engineers**: Learning ASPICE requirements and best practices
- **Assessors**: Preparing for formal ASPICE assessments

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) OpenAI API key for enhanced AI responses

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd ASPICE-Capability-Checker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Optional: Configure OpenAI API**
   ```bash
   cp .env.example .env
   # Edit .env file and add your OPENAI_API_KEY
   ```
   
   **Note**: Without an API key, the tool uses a built-in rule-based engine that works entirely offline.

### Launching the Application

#### Web Interface (Recommended)
```bash
streamlit run app.py
```
The application will open in your default browser at `http://localhost:8501`

#### Command-Line Interface
```bash
python cli.py <command>
```
See [CLI section](#7-command-line-interface-cli) for detailed commands.

---

## Features and Use Cases

### 1. ASPICE Q&A Chat

**What it does**: Answers natural language questions about ASPICE v4.0 using semantic search over the knowledge base.

#### Use Cases

##### Use Case 1.1: Learning About ASPICE Levels
**Scenario**: A new team member needs to understand capability levels.

**Steps**:
1. Navigate to **💬 ASPICE Q&A Chat** page
2. Click quick question "What is ASPICE Level 2?" or type your own question
3. Review the answer with retrieved ASPICE context

**Example Questions**:
- "What is ASPICE Level 2?"
- "Explain the difference between Level 3 and Level 4"
- "What is the rating scale in ASPICE?"

**Expected Output**: Detailed explanation with references to ASPICE v4.0 standards.

---

##### Use Case 1.2: Understanding Process Requirements
**Scenario**: A developer needs to know what work products SWE.1 requires.

**Steps**:
1. Go to **💬 ASPICE Q&A Chat**
2. Type: "What work products does SWE.1 require?"
3. Review the list of required work products

**Example Questions**:
- "What are SWE.1 base practices?"
- "What work products does SUP.8 require?"
- "What outcomes are expected from MAN.3?"

**Expected Output**: Comprehensive list with explanations from ASPICE v4.0.

---

##### Use Case 1.3: Understanding Process Attributes
**Scenario**: An assessor needs clarification on how PA 3.1 is assessed.

**Steps**:
1. Open **💬 ASPICE Q&A Chat**
2. Ask: "How is PA 3.1 assessed?"
3. Read the detailed assessment criteria and indicators

**Example Questions**:
- "How is PA 3.1 assessed?"
- "What are the indicators for PA 2.2?"
- "What's the difference between PA 2.1 and PA 2.2?"

**Expected Output**: Assessment indicators and guidance for the process attribute.

---

##### Use Case 1.4: Comparing Processes
**Scenario**: Understanding differences between similar processes.

**Steps**:
1. Navigate to chat interface
2. Type: "What's the difference between SWE.1 and SYS.1?"
3. Review the comparative explanation

**Expected Output**: Clear comparison highlighting key differences.

---

### 2. Single Process Capability Assessment

**What it does**: Assesses a single ASPICE process and determines its achieved capability level based on Process Attribute (PA) ratings.

#### Use Cases

##### Use Case 2.1: Basic Process Assessment
**Scenario**: A quality manager needs to assess SWE.1 (Software Requirements Analysis) for a project.

**Steps**:
1. Navigate to **📊 Capability Assessment**
2. Select "SWE.1" from the process dropdown
3. Read the process information displayed
4. Set target capability level (e.g., 3)
5. Rate each Process Attribute:
   - PA 1.1: F (Fully achieved)
   - PA 2.1: L (Largely achieved)
   - PA 2.2: F (Fully achieved)
   - PA 3.1: P (Partially achieved)
   - PA 3.2: N (Not achieved)
6. Click **🔍 Assess Capability**

**Expected Output**:
- Capability level gauge showing achieved level (2 in this case)
- Level description: "Managed"
- PA ratings table with color coding
- Identified gaps: "PA 2.1 is only Largely achieved; must be Fully achieved for Level 2"
- Recommendations: "Strengthen PA 2.1 to reach Level 2" and "Address PA 3.1 and PA 3.2 to progress to Level 3"

---

##### Use Case 2.2: Assessment with Checklist Verification
**Scenario**: Team lead wants to verify their PA ratings using assessment questions.

**Steps**:
1. Go to **📊 Capability Assessment**
2. Select process (e.g., "MAN.3")
3. Rate all Process Attributes
4. Click **🔍 Assess Capability**
5. Expand **📋 Assessment Checklist Questions**
6. Review questions for each PA to verify your ratings

**Expected Output**:
- Standard assessment output
- Expandable checklist showing specific assessment questions for each PA
- Use these questions to validate your initial ratings

---

##### Use Case 2.3: Target Level Planning
**Scenario**: Planning what's needed to achieve a specific capability level.

**Steps**:
1. Select your process
2. Adjust target level slider (e.g., set to Level 4)
3. Enter current PA ratings
4. Review gaps and recommendations focused on achieving Level 4

**Expected Output**:
- Clear identification of which PAs need improvement
- Specific actions required to reach target level

---

### 3. Multi-Process Assessment

**What it does**: Assesses multiple ASPICE processes simultaneously and provides comparative analysis with visualizations.

#### Use Cases

##### Use Case 3.1: Project-Wide Assessment
**Scenario**: Quality manager needs to assess all key processes for an automotive project.

**Steps**:
1. Navigate to **📋 Multi-Process Assessment**
2. Go to **⌨️ Manual Input** tab
3. Select processes: SWE.1, SWE.2, SWE.3, MAN.3, SUP.1, SUP.8
4. For each process, expand and rate Process Attributes:
   ```
   SWE.1: PA 1.1=F, PA 2.1=F, PA 2.2=F, PA 3.1=L, PA 3.2=P
   SWE.2: PA 1.1=F, PA 2.1=F, PA 2.2=L, PA 3.1=N, PA 3.2=N
   SWE.3: PA 1.1=F, PA 2.1=L, PA 2.2=F, PA 3.1=N, PA 3.2=N
   MAN.3: PA 1.1=F, PA 2.1=F, PA 2.2=F, PA 3.1=L, PA 3.2=L
   SUP.1: PA 1.1=F, PA 2.1=F, PA 2.2=F, PA 3.1=F, PA 3.2=F
   SUP.8: PA 1.1=F, PA 2.1=L, PA 2.2=F, PA 3.1=N, PA 3.2=N
   ```
5. Click **🔍 Assess All Processes**

**Expected Output**:
- Summary metrics:
  - Processes Assessed: 6
  - Average Level: 2.5
  - Min Level: 2
  - Max Level: 3
- Bar chart showing capability levels by process
- Radar chart showing capability profile
- Expandable per-process details with gaps and recommendations

---

##### Use Case 3.2: JSON Import for Automated Assessment
**Scenario**: Importing assessment data from another tool or spreadsheet.

**Steps**:
1. Go to **📋 Multi-Process Assessment**
2. Switch to **📄 JSON Import** tab
3. Paste JSON data:
   ```json
   {
     "SWE.1": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F", "PA 3.1": "L", "PA 3.2": "P"},
     "SWE.2": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "L"},
     "MAN.3": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"}
   }
   ```
4. Click **📥 Import & Assess**

**Expected Output**:
- Same comprehensive assessment as manual input
- Faster for bulk assessments or scripted workflows

---

##### Use Case 3.3: Comparative Process Analysis
**Scenario**: Comparing maturity across different process areas (SWE vs MAN vs SUP).

**Steps**:
1. Select representative processes from each area
2. Perform multi-process assessment
3. Analyze radar chart to see maturity profile
4. Use bar chart to identify lowest-capability processes

**Expected Output**:
- Visual comparison showing which process areas are strongest/weakest
- Insights for prioritizing improvement efforts

---

### 4. Improvement Roadmap

**What it does**: Generates a step-by-step improvement plan to reach a target capability level, with gap analysis and specific actions for each process.

#### Use Cases

##### Use Case 4.1: Planning Level 3 Achievement
**Scenario**: Organization currently at Level 2 wants to achieve Level 3 for key processes.

**Steps**:
1. Navigate to **🗺️ Improvement Roadmap**
2. Set target capability level: 3
3. Select processes: SWE.1, SWE.2, MAN.3, SUP.1
4. Rate current state for each process:
   ```
   SWE.1: PA 1.1=F, PA 2.1=F, PA 2.2=F, PA 3.1=P, PA 3.2=N
   SWE.2: PA 1.1=F, PA 2.1=F, PA 2.2=L, PA 3.1=N, PA 3.2=N
   MAN.3: PA 1.1=F, PA 2.1=F, PA 2.2=F, PA 3.1=L, PA 3.2=P
   SUP.1: PA 1.1=F, PA 2.1=F, PA 2.2=F, PA 3.1=F, PA 3.2=F
   ```
5. Click **🗺️ Generate Roadmap**

**Expected Output**:
For each process:
- ✅ SUP.1: Target already achieved (Level 3)
- 🔧 SWE.1: Current Level 2 → Target Level 3
  1. Achieve PA 3.1 (Process Definition): Document standard process
  2. Achieve PA 3.2 (Process Deployment): Deploy standard process across projects
- 🔧 SWE.2: Current Level 1 → Target Level 3
  1. Achieve PA 2.1 Fully: Implement planning and monitoring
  2. Achieve PA 2.2 Fully: Implement work product management
  3. Achieve PA 3.1: Define standard architectural design process
  4. Achieve PA 3.2: Deploy process organization-wide
- 🔧 MAN.3: Current Level 2 → Target Level 3
  1. Achieve PA 3.1 Fully: Complete process definition
  2. Achieve PA 3.2 Fully: Full deployment of standard process

---

##### Use Case 4.2: Incremental Improvement Planning
**Scenario**: Planning realistic incremental improvements over multiple assessment cycles.

**Steps**:
1. Start with target Level 2 (if currently at 1)
2. Generate roadmap and implement actions
3. Re-assess after implementation
4. Generate new roadmap with target Level 3
5. Continue iteratively

**Expected Output**:
- Realistic, achievable action plans for each cycle
- Clear progress tracking between assessments

---

##### Use Case 4.3: Supplier Development Planning
**Scenario**: Helping a supplier improve their process capability.

**Steps**:
1. Assess supplier's current processes
2. Define contractual target level (e.g., Level 2 for all SWE processes)
3. Generate improvement roadmap
4. Share actionable steps with supplier
5. Monitor progress in subsequent assessments

**Expected Output**:
- Clear development plan for supplier
- Specific actions that can be tracked and verified

---

### 5. ASPICE Knowledge Base Browser

**What it does**: Provides structured browsing of ASPICE v4.0 standards including processes, capability levels, and assessment questions.

#### Use Cases

##### Use Case 5.1: Learning Process Details
**Scenario**: Developer wants to understand SWE.4 (Software Unit Verification) requirements.

**Steps**:
1. Navigate to **📚 ASPICE Knowledge Base**
2. Go to **🏗️ Processes** tab
3. Filter by "SWE" (Software Engineering)
4. Expand "SWE.4 — Software Unit Verification"

**Expected Output**:
- Purpose: Verify software units against requirements
- Outcomes: List of expected outcomes
- Work Products: Required documentation and artifacts
- Base Practices: Specific activities to perform

---

##### Use Case 5.2: Understanding Capability Levels
**Scenario**: Team lead needs to explain capability levels to the team.

**Steps**:
1. Go to **📚 ASPICE Knowledge Base**
2. Switch to **📏 Capability Levels** tab
3. Review each level (0-5) with descriptions
4. Expand Process Attributes to see details and indicators

**Expected Output**:
- Complete overview of all 6 capability levels
- Description of each level's characteristics
- Process Attributes with detailed indicators for each level

---

##### Use Case 5.3: Preparing for Assessment
**Scenario**: Assessor preparing assessment questions for upcoming audit.

**Steps**:
1. Navigate to **📚 ASPICE Knowledge Base**
2. Go to **❓ Assessment Questions** tab
3. Select PA (e.g., "PA 2.1")
4. Review comprehensive list of assessment questions

**Expected Output**:
- Specific questions to verify PA achievement
- Use these as checklist during actual assessment

---

##### Use Case 5.4: Process Group Overview
**Scenario**: Understanding all processes in a specific area.

**Steps**:
1. Go to **🏗️ Processes** tab
2. Filter by process group (SWE, SYS, MAN, SUP, or ACQ)
3. Browse all processes in that group

**Expected Output**:
- Complete view of all processes in the selected domain
- Easy comparison of similar processes

---

### 6. Knowledge Enhancement

**What it does**: Allows adding organization-specific knowledge to the agent, including process tailoring guidelines, lessons learned, and custom procedures.

#### Use Cases

##### Use Case 6.1: Adding Tool-Specific Guidance
**Scenario**: Organization uses DOORS NG for requirements management and wants to add tool-specific guidance.

**Steps**:
1. Navigate to **🧠 Knowledge Enhancement**
2. In **Document Title / ID**, enter: "SWE1_DOORS_Guidelines"
3. In **Knowledge Content**, paste:
   ```
   SWE.1 Requirements Management with DOORS NG:
   - All requirements must be stored in DOORS NG with unique REQ-ID format
   - Requirement IDs follow pattern: REQ-<module>-<sequence>
   - Traceability to system requirements is mandatory via trace links
   - Requirements must have attributes: Priority, Status, Verification Method
   - Review workflow: Draft → Under Review → Approved → Baseline
   - Change requests tracked in DOORS via formal change request module
   ```
4. Click **📥 Add to Knowledge Base**

**Expected Output**:
- Success message: "✅ Knowledge added and index updated!"
- Document appears in "Added Custom Knowledge" list
- Agent can now answer questions using this knowledge

**Testing**:
- In "Test Enhanced Knowledge" section, ask: "How do we manage requirements in DOORS?"
- Agent will respond using your custom knowledge

---

##### Use Case 6.2: ISO 26262 Functional Safety Integration
**Scenario**: Automotive safety team needs ASPICE processes aligned with ISO 26262.

**Steps**:
1. Go to **🧠 Knowledge Enhancement**
2. Select template: "Functional Safety (ISO 26262) Overlay"
3. Click **📋 Load Template**
4. Review pre-filled content
5. Copy content to main text area and customize for your organization
6. Add to knowledge base

**Expected Output**:
- Template loaded with ISO 26262 mappings
- Agent can answer questions about ASPICE-Safety integration
- Example query: "What ASPICE level is required for ASIL C projects?"

---

##### Use Case 6.3: Agile-ASPICE Integration
**Scenario**: Agile team needs guidance on mapping Scrum practices to ASPICE.

**Steps**:
1. Navigate to **🧠 Knowledge Enhancement**
2. Select template: "Agile-ASPICE Bridge Notes"
3. Load and customize template
4. Add specific team practices
5. Add to knowledge base

**Expected Output**:
- Mapping between Agile ceremonies and ASPICE processes
- Guidance on satisfying ASPICE in Agile context
- Example query: "How does sprint planning relate to ASPICE?"

---

##### Use Case 6.4: Lessons Learned from Previous Assessments
**Scenario**: Capturing and sharing lessons from past ASPICE assessments.

**Steps**:
1. Go to **🧠 Knowledge Enhancement**
2. Document Title: "Assessment_Lessons_Learned_2024"
3. Add content:
   ```
   Lessons Learned from Q2 2024 ASPICE Assessment:
   
   Strengths:
   - PA 2.2 work product management well-established using Git and Jira
   - SUP.8 configuration management received F ratings across all projects
   
   Gaps Found:
   - SWE.1: Requirement reviews not consistently documented
   - MAN.3: Project monitoring metrics not regularly analyzed
   - SUP.1: QA audit schedules not maintained
   
   Actions Taken:
   - Implemented mandatory review checklist in requirements tool
   - Created automated dashboard for project metrics
   - Set up recurring calendar reminders for QA audits
   
   Recommendations for Next Assessment:
   - Gather evidence continuously, not just before assessment
   - Maintain traceability matrices in real-time
   - Regular internal audits to identify gaps early
   ```
4. Add to knowledge base

**Expected Output**:
- Institutional knowledge preserved and searchable
- Team can query: "What gaps did we have in SWE.1 last time?"
- Prevents repeating past mistakes

---

##### Use Case 6.5: Supplier Assessment Criteria
**Scenario**: Defining specific criteria for assessing suppliers.

**Steps**:
1. Load template: "Supplier Assessment Checklist"
2. Customize with company-specific requirements
3. Add to knowledge base
4. Use in supplier evaluations

**Expected Output**:
- Standardized supplier assessment approach
- Query: "What should we check in supplier assessment?" returns your criteria

---

### 7. Command-Line Interface (CLI)

**What it does**: Provides command-line access to all agent features for scripting, automation, and non-GUI workflows.

#### Use Cases

##### Use Case 7.1: Interactive Q&A Session
**Scenario**: Quick command-line queries about ASPICE.

**Command**:
```bash
python cli.py chat
```

**Usage**:
```
💬 ASPICE Q&A Chat — type 'quit' to exit

You: What is ASPICE Level 2?

Agent:
ASPICE Level 2 (Managed) means that the process is performed and managed.
It includes PA 1.1 (Process Performance) plus:
- PA 2.1 (Performance Management): Planning and monitoring
- PA 2.2 (Work Product Management): Work products are managed
...

You: What are SWE.1 outcomes?

Agent:
SWE.1 outcomes include:
1. Software requirements are identified and documented
2. Requirements are analyzed for correctness and testability
...

You: quit
```

---

##### Use Case 7.2: Single Process Assessment via CLI
**Scenario**: Quick assessment of a process with interactive PA rating input.

**Command**:
```bash
python cli.py assess --process SWE.1
```

**Usage**:
```
📊 Assessing process: SWE.1

Rate each Process Attribute (N / P / L / F):
  PA 1.1: F
  PA 2.1: F
  PA 2.2: F
  PA 3.1: L
  PA 3.2: N
  PA 4.1: N
  PA 4.2: N
  PA 5.1: N
  PA 5.2: N

=======================================================
  Process  : SWE.1
  Level    : 2 — Managed
=======================================================

⚠️  Gaps:
  • To reach Level 3, both PA 3.1 and PA 3.2 must be L or F

💡 Recommendations:
  • Achieve PA 3.1 (Process Definition) by documenting standard process
  • Achieve PA 3.2 (Process Deployment) by deploying across organization
```

---

##### Use Case 7.3: Scripted Assessment with JSON Input
**Scenario**: Automated assessment as part of CI/CD pipeline or batch processing.

**Command**:
```bash
python cli.py assess --process SWE.1 --ratings '{"PA 1.1":"F","PA 2.1":"F","PA 2.2":"F","PA 3.1":"L","PA 3.2":"N"}'
```

**Expected Output**:
Same as interactive assessment but fully automated - suitable for scripts.

---

##### Use Case 7.4: Improvement Roadmap Generation
**Scenario**: Planning improvements for multiple processes.

**Command**:
```bash
python cli.py roadmap --target 3 --processes SWE.1 SWE.2 MAN.3
```

**Usage**:
```
🗺️  Improvement Roadmap — Target Level 3

Rate PAs for SWE.1 (N/P/L/F):
  PA 1.1: F
  PA 2.1: F
  PA 2.2: F
  PA 3.1: P
  PA 3.2: N

Rate PAs for SWE.2 (N/P/L/F):
  PA 1.1: F
  PA 2.1: L
  PA 2.2: F
  PA 3.1: N
  PA 3.2: N

Rate PAs for MAN.3 (N/P/L/F):
  PA 1.1: F
  PA 2.1: F
  PA 2.2: F
  PA 3.1: F
  PA 3.2: F

=======================================================
  Target: Capability Level 3
=======================================================

  ✅ MAN.3: Target already achieved (Level 3)

  🔧 SWE.1: Current Level 2 → Target Level 3
     1. Achieve PA 3.1 Fully: Complete process definition
     2. Achieve PA 3.2: Deploy standard process

  🔧 SWE.2: Current Level 1 → Target Level 3
     1. Achieve PA 2.1 Fully: Complete performance management
     2. Achieve PA 3.1: Define standard process
     3. Achieve PA 3.2: Deploy standard process
```

---

##### Use Case 7.5: Viewing Capability Levels Reference
**Scenario**: Quick reference to capability level definitions.

**Command**:
```bash
python cli.py levels
```

**Expected Output**:
```
📏 ASPICE v4.0 Capability Levels

  Level 0: Incomplete
    The process is not implemented or fails to achieve its purpose…
  
  Level 1: Performed
    The process achieves its purpose. Process outcomes are achieved…
    ├ PA 1.1 — Process Performance
  
  Level 2: Managed
    The process is performed and managed (planned, monitored, adjusted)…
    ├ PA 2.1 — Performance Management
    ├ PA 2.2 — Work Product Management
  
  ...
```

---

##### Use Case 7.6: Getting Process Information
**Scenario**: Looking up details about a specific process.

**Command**:
```bash
python cli.py info --process MAN.3
```

**Expected Output**:
```
=======================================================
  MAN.3 — Project Management
  Group: Management
=======================================================

Purpose:
  To identify, establish, and control project activities and resources...

Outcomes:
  • Project scope is defined
  • Project activities and resources are sized and estimated
  • Project schedule is defined and maintained
  ...

Work Products:
  • Project plan
  • Work breakdown structure
  • Schedule
  ...

Base Practices:
  • Define project scope
  • Define project activities
  • Estimate project resources
  ...
```

---

### 8. Programmatic API

**What it does**: Python API for integrating ASPICE assessment into custom tools, scripts, or applications.

#### Use Cases

##### Use Case 8.1: Integration into Custom Dashboard
**Scenario**: Building a company dashboard that includes ASPICE capability metrics.

**Code**:
```python
from src.rag_engine import AspiceAgent

# Initialize agent
agent = AspiceAgent()
agent.build_knowledge_base()

# Assess multiple processes
current_state = {
    "SWE.1": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"},
    "SWE.2": {"PA 1.1": "F", "PA 2.1": "L", "PA 2.2": "F"},
    "MAN.3": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"},
}

results = agent.assess_multiple_processes(current_state)

# Extract metrics for dashboard
print(f"Average Capability Level: {results['summary']['average_capability_level']}")
print(f"Processes at Level 2+: {sum(1 for r in results['results'].values() if r['achieved_level'] >= 2)}")

# Display per-process results
for proc_id, result in results['results'].items():
    print(f"{proc_id}: Level {result['achieved_level']} - {result['level_name']}")
```

---

##### Use Case 8.2: Automated Reporting
**Scenario**: Generating monthly ASPICE capability reports.

**Code**:
```python
from src.rag_engine import AspiceAgent
import json
from datetime import datetime

agent = AspiceAgent()
agent.build_knowledge_base()

# Load assessment data (could be from database, spreadsheet, etc.)
with open('monthly_assessment_data.json', 'r') as f:
    assessment_data = json.load(f)

# Perform assessment
results = agent.assess_multiple_processes(assessment_data)

# Generate report
report = {
    "date": datetime.now().isoformat(),
    "summary": results['summary'],
    "details": []
}

for proc_id, result in results['results'].items():
    report['details'].append({
        "process": proc_id,
        "level": result['achieved_level'],
        "level_name": result['level_name'],
        "gaps": result['gaps'],
        "recommendations": result['recommendations']
    })

# Save report
with open(f'aspice_report_{datetime.now().strftime("%Y%m%d")}.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Report generated successfully!")
```

---

##### Use Case 8.3: Q&A Bot Integration
**Scenario**: Adding ASPICE knowledge to Slack/Teams bot.

**Code**:
```python
from src.rag_engine import AspiceAgent

class AspiceBot:
    def __init__(self):
        self.agent = AspiceAgent()
        self.agent.build_knowledge_base()
    
    def handle_question(self, user_question: str) -> str:
        """Handle user questions about ASPICE"""
        answer = self.agent.chat(user_question)
        return answer
    
    def assess_process(self, process_id: str, pa_ratings: dict) -> str:
        """Assess a process and return formatted response"""
        result = self.agent.assess_process(process_id, pa_ratings)
        
        response = f"Assessment Results for {process_id}:\n"
        response += f"Achieved Level: {result['achieved_level']} - {result['level_name']}\n\n"
        
        if result['gaps']:
            response += "Gaps:\n"
            for gap in result['gaps']:
                response += f"  • {gap}\n"
        
        return response

# Usage in bot
bot = AspiceBot()
response = bot.handle_question("What is ASPICE Level 2?")
print(response)
```

---

##### Use Case 8.4: Custom Knowledge Enhancement
**Scenario**: Programmatically adding knowledge from external sources.

**Code**:
```python
from src.rag_engine import AspiceAgent
import json

agent = AspiceAgent()
agent.build_knowledge_base()

# Load organization-specific documents
with open('company_process_descriptions.json', 'r') as f:
    company_processes = json.load(f)

# Add each document to knowledge base
for doc_id, content in company_processes.items():
    agent.add_custom_knowledge(
        text=content,
        doc_id=doc_id
    )
    print(f"Added: {doc_id}")

# Test enhanced knowledge
answer = agent.chat("How does our company implement SWE.1?")
print(answer)
```

---

##### Use Case 8.5: Improvement Tracking Over Time
**Scenario**: Tracking capability improvement across multiple assessment cycles.

**Code**:
```python
from src.rag_engine import AspiceAgent
import json
from datetime import datetime

agent = AspiceAgent()
agent.build_knowledge_base()

# Historical assessments
assessments = [
    {
        "date": "2024-Q1",
        "data": {"SWE.1": {"PA 1.1": "F", "PA 2.1": "L"}}
    },
    {
        "date": "2024-Q2",
        "data": {"SWE.1": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "L"}}
    },
    {
        "date": "2024-Q3",
        "data": {"SWE.1": {"PA 1.1": "F", "PA 2.1": "F", "PA 2.2": "F"}}
    }
]

# Track progress
progress = []
for assessment in assessments:
    result = agent.assess_process("SWE.1", assessment['data'])
    progress.append({
        "date": assessment['date'],
        "level": result['achieved_level'],
        "level_name": result['level_name']
    })

# Display trend
print("SWE.1 Capability Trend:")
for p in progress:
    print(f"  {p['date']}: Level {p['level']} ({p['level_name']})")
```

---

## Understanding ASPICE

### What is ASPICE?
Automotive SPICE® (Software Process Improvement and Capability dEtermination) is a framework for assessing and improving software development processes in the automotive industry. Version 4.0 is the latest standard.

### Capability Levels

| Level | Name | Description | Key Requirements |
|-------|------|-------------|------------------|
| **0** | Incomplete | Process not implemented or fails to achieve purpose | — |
| **1** | Performed | Process achieves its purpose | PA 1.1: Process outcomes achieved |
| **2** | Managed | Process is planned, monitored, and controlled | PA 1.1 + PA 2.1 (Planning) + PA 2.2 (Work Product Mgmt) |
| **3** | Established | Process uses defined standard process | Level 2 + PA 3.1 (Process Definition) + PA 3.2 (Deployment) |
| **4** | Predictable | Process operates within quantitative limits | Level 3 + PA 4.1 (Quantitative Analysis) + PA 4.2 (Control) |
| **5** | Optimizing | Process continuously improved based on measurement | Level 4 + PA 5.1 (Innovation) + PA 5.2 (Optimization) |

### Rating Scale

Process Attributes (PAs) are rated using a 4-point scale:

| Rating | Name | Achievement Range | Meaning |
|--------|------|-------------------|---------|
| **N** | Not achieved | 0-15% | Little or no evidence |
| **P** | Partially achieved | 15-50% | Some evidence, systematic approach lacking |
| **L** | Largely achieved | 50-85% | Systematic approach, some weaknesses remain |
| **F** | Fully achieved | 85-100% | Complete, comprehensive evidence |

### Capability Level Rules

To achieve a capability level, you must:
1. **Fully achieve (F)** all Process Attributes of that level AND all lower levels
2. Exception: At Level 1, only need PA 1.1 = L or F
3. Exception: At Level 2, can have one PA at L, but prefer both F

Examples:
- **Level 1**: PA 1.1 = L or F
- **Level 2**: PA 1.1 = F, PA 2.1 = F, PA 2.2 = F (or one PA = L)
- **Level 3**: All Level 2 PAs = F, PA 3.1 = F, PA 3.2 = F

### Process Areas

#### SWE (Software Engineering)
- SWE.1: Software Requirements Analysis
- SWE.2: Software Architectural Design
- SWE.3: Software Detailed Design and Unit Construction
- SWE.4: Software Unit Verification
- SWE.5: Software Integration and Integration Test
- SWE.6: Software Qualification Test

#### SYS (System Engineering)
- SYS.1: Requirements Elicitation
- SYS.2: System Requirements Analysis
- SYS.3: System Architectural Design
- SYS.4: System Integration and Integration Test
- SYS.5: System Qualification Test

#### MAN (Management)
- MAN.3: Project Management
- MAN.5: Risk Management
- MAN.6: Measurement

#### SUP (Support)
- SUP.1: Quality Assurance
- SUP.8: Configuration Management
- SUP.9: Problem Resolution Management
- SUP.10: Change Request Management

#### ACQ (Acquisition)
- ACQ.4: Supplier Monitoring

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Knowledge Base Build Fails
**Symptom**: Error during `agent.build_knowledge_base()`

**Solutions**:
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Ensure sentence-transformers model downloads successfully
- Check internet connection for first-time model download
- Verify Python version >= 3.8

---

#### Issue 2: OpenAI API Key Not Working
**Symptom**: Error "Invalid API key" or no GPT responses

**Solutions**:
- Verify API key is correct in `.env` file
- Ensure format: `OPENAI_API_KEY=sk-...`
- Check API key hasn't expired
- Test without API key (uses built-in engine)
- Restart application after adding API key

---

#### Issue 3: Streamlit App Won't Start
**Symptom**: Error when running `streamlit run app.py`

**Solutions**:
```bash
# Reinstall streamlit
pip uninstall streamlit
pip install streamlit

# Check if port 8501 is already in use
streamlit run app.py --server.port 8502

# Clear streamlit cache
streamlit cache clear
```

---

#### Issue 4: Assessment Results Unexpected
**Symptom**: Capability level doesn't match expectations

**Solutions**:
- Review ASPICE capability level rules (see [Understanding ASPICE](#understanding-aspice))
- Check that you understand rating scale (N/P/L/F)
- Remember: Both PA 2.1 AND PA 2.2 must be F for solid Level 2
- Remember: All lower-level PAs must be F to achieve higher levels
- Use assessment questions to verify your PA ratings

---

#### Issue 5: CLI Commands Not Working
**Symptom**: `python cli.py` gives errors

**Solutions**:
```bash
# Ensure you're in correct directory
cd /path/to/ASPICE-Capability-Checker

# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt

# Try with python3 explicitly
python3 cli.py chat
```

---

#### Issue 6: JSON Import Fails
**Symptom**: "Invalid JSON" error in multi-process assessment

**Solutions**:
- Validate JSON syntax at jsonlint.com
- Ensure double quotes (not single quotes) for JSON
- Check PA names are exact: "PA 1.1", "PA 2.1", etc.
- Verify rating values are one of: "N", "P", "L", "F"

**Valid JSON example**:
```json
{
  "SWE.1": {
    "PA 1.1": "F",
    "PA 2.1": "F"
  }
}
```

---

#### Issue 7: Custom Knowledge Not Being Used
**Symptom**: Agent doesn't use added custom knowledge

**Solutions**:
- Verify success message after adding knowledge
- Try more specific questions that relate to your custom content
- Ensure custom text has sufficient detail
- Check that document was added to current session
- Restart session if knowledge was added in previous session

---

#### Issue 8: Slow Performance
**Symptom**: Agent responses take too long

**Solutions**:
- First run is slower (downloads ML models)
- Subsequent runs should be faster
- Without OpenAI API: Responses are instant (rule-based)
- With OpenAI API: Depends on API response time
- Consider increasing system RAM if running locally
- Close other applications to free resources

---

## Best Practices

### For Assessment Preparation

1. **Gather Evidence First**
   - Collect all work products, records, and artifacts before starting assessment
   - Review project documentation for each process
   - Interview team members about actual practices

2. **Use Assessment Questions**
   - Review questions in Knowledge Base → Assessment Questions tab
   - Use questions as checklist for evidence gathering
   - Don't rate PAs as "F" unless you can answer most questions positively

3. **Start with Process Information**
   - Review process details in Knowledge Base before assessing
   - Understand outcomes, work products, and base practices
   - Ensure you're assessing actual implementation, not intentions

4. **Be Conservative with Ratings**
   - When in doubt, rate lower (L instead of F, P instead of L)
   - "Fully achieved" means 85-100% with comprehensive evidence
   - Partial implementation is still "Partially achieved"

5. **Document Gaps**
   - Use agent's recommendations as starting point
   - Document specific evidence gaps
   - Create action items for addressing each gap

### For Improvement Planning

1. **Incremental Approach**
   - Target one level at a time
   - Solidify current level before moving to next
   - Use improvement roadmap for step-by-step plan

2. **Focus on Weakest Areas**
   - Multi-process assessment reveals lowest-capability processes
   - Prioritize processes critical to your projects
   - Address systemic issues affecting multiple processes

3. **Leverage Custom Knowledge**
   - Add lessons learned from past improvements
   - Document what worked and what didn't
   - Share successful practices across teams

4. **Regular Monitoring**
   - Reassess quarterly or after major process changes
   - Track trend over time using programmatic API
   - Celebrate improvements and address regressions

5. **Involve the Team**
   - Share assessment results with development team
   - Get team input on improvement actions
   - Assign owners for each improvement activity

### For Knowledge Enhancement

1. **Start with Templates**
   - Use provided templates as starting point
   - Customize for your organization
   - Maintain consistent format

2. **Add Incrementally**
   - Don't try to add everything at once
   - Add knowledge as you use the tool
   - Focus on frequently asked questions

3. **Keep It Current**
   - Update custom knowledge when processes change
   - Remove obsolete information
   - Date your knowledge entries

4. **Test Your Knowledge**
   - Use "Test Enhanced Knowledge" feature
   - Verify agent can retrieve your custom content
   - Refine wording if answers aren't as expected

### For CLI and Automation

1. **Script Repetitive Tasks**
   - Use JSON input for repeated assessments
   - Create shell scripts for common workflows
   - Save assessment data in version control

2. **Integrate with CI/CD**
   - Run assessments as part of release process
   - Track capability metrics in your dashboard
   - Alert on capability regressions

3. **Maintain Assessment History**
   - Save JSON assessment data with timestamps
   - Track improvements over time
   - Use for trend analysis and reporting

---

## FAQ

### General Questions

**Q: Do I need an OpenAI API key to use this tool?**
A: No. The tool works fully offline using a built-in rule-based engine and semantic search. The OpenAI API key is optional and only enhances natural language responses.

**Q: Can I use this for non-automotive projects?**
A: Yes, while ASPICE is automotive-focused, the process assessment framework applies to any software development. The core concepts (managed processes, process definition, measurement) are universal.

**Q: Is this tool officially endorsed by VDA or ASPICE?**
A: No. This is an independent tool to help teams understand and prepare for ASPICE assessments. It's not a replacement for formal ASPICE assessments by certified assessors.

**Q: Can this tool perform official ASPICE certifications?**
A: No. This tool helps with preparation and self-assessment. Official ASPICE certifications must be conducted by certified assessors from accredited organizations.

### Assessment Questions

**Q: Why did I get Level 1 when I rated several PAs as F?**
A: To achieve Level 2, ALL of PA 1.1, PA 2.1, and PA 2.2 must be L or F (preferably F). Check if any of these PAs are rated N or P.

**Q: What's the difference between "Largely" and "Fully" achieved?**
A: Largely (L) = 50-85% achievement with some weaknesses. Fully (F) = 85-100% with comprehensive evidence. For higher capability levels, F is usually required.

**Q: Can I achieve Level 3 if I skip Level 2?**
A: No. Capability levels are cumulative. To achieve Level 3, you must first fully achieve Level 2 (all PAs of Level 1 and 2 must be F), then achieve PA 3.1 and PA 3.2.

**Q: How many processes do I need to assess?**
A: It depends on your project scope. Typically assess all processes relevant to your development activities. For software projects, at minimum: SWE.1-6, MAN.3, SUP.1, SUP.8, SUP.10.

**Q: Should I assess each project separately?**
A: If projects follow the same organizational processes, one assessment may suffice. If projects use different processes or have different maturity levels, assess separately.

### Technical Questions

**Q: Can I export assessment results?**
A: Currently through CLI/API you can save JSON results. For UI, use screenshots or copy text. Future versions may add export features.

**Q: Can multiple users use this simultaneously?**
A: The Streamlit web UI is single-user per instance. For multi-user, deploy multiple instances or use the programmatic API to build a custom multi-user interface.

**Q: How is my data stored?**
A: All data is stored locally on your machine. The vector database (FAISS index) is in memory. Custom knowledge is added to the session only. No data is sent externally (except OpenAI API if configured).

**Q: Can I customize the ASPICE knowledge base?**
A: The core ASPICE v4.0 knowledge is fixed. However, you can add unlimited custom knowledge using the Knowledge Enhancement feature, which augments (not replaces) the base knowledge.

**Q: What machine learning models are used?**
A: The tool uses `sentence-transformers` library with the `all-MiniLM-L6-v2` model for semantic search. It's a lightweight model that runs on CPU. FAISS is used for efficient similarity search.

### Process-Specific Questions

**Q: What if my process doesn't fit standard ASPICE processes?**
A: Map your process to the closest ASPICE process based on purpose and outcomes. Use custom knowledge to document your mapping. Example: Map your "Code Review Process" to SUP.1 (Quality Assurance).

**Q: We use Agile - can we still use ASPICE?**
A: Absolutely! Use the "Agile-ASPICE Bridge Notes" template. Many Agile practices map to ASPICE processes. For example:
- Sprint Planning → MAN.3 (Project Management)
- User Stories → SWE.1 (Requirements Analysis)
- Sprint Retrospectives → Process improvement (PA 5.2)

**Q: How do we handle processes not in our scope?**
A: Only assess processes relevant to your projects. For example, if you don't do acquisition, skip ACQ.4. Document your scope clearly.

**Q: What about system engineering processes (SYS.x)?**
A: If you develop embedded systems with both hardware and software, assess SYS processes in addition to SWE. If you're pure software, focus on SWE processes.

### Improvement Questions

**Q: How long does it take to improve from Level 1 to Level 2?**
A: Typically 3-6 months with dedicated effort. It requires implementing planning, monitoring, and work product management practices systematically.

**Q: What's the minimum capability level required for automotive projects?**
A: Many OEMs require Level 2 for all SWE processes. Some critical projects require Level 3. Check your specific customer requirements.

**Q: Should we target Level 5 for all processes?**
A: Not necessarily. Level 3 is sufficient for most automotive projects. Levels 4-5 are for organizations doing process innovation and optimization. Focus on solid Level 2-3 achievement first.

**Q: Can we improve multiple processes in parallel?**
A: Yes, but it's challenging. Better to focus on 2-3 critical processes, achieve target level, then expand to others. Spreading resources too thin reduces effectiveness.

---

## Additional Resources

### ASPICE Standards
- Automotive SPICE® v4.0 Process Assessment Model (PAM) - Available from VDA QMC
- ISO/IEC 33020: Process measurement framework
- ISO/IEC 33001: Concepts and terminology

### Related Standards
- ISO 26262: Functional Safety for automotive systems
- ISO/IEC 15504: Process assessment (SPICE foundation)
- CMMI: Alternative process improvement framework

### Training and Certification
- VDA QMC: Official ASPICE training and assessor certification
- SGS TÜV: ASPICE assessment services
- Professional ASPICE training providers

### Online Communities
- ASPICE user groups and forums
- LinkedIn ASPICE groups
- Automotive software engineering communities

---

## Getting Help

### Tool-Related Issues
- Check this user manual first
- Review [Troubleshooting](#troubleshooting) section
- Check project README.md for latest updates
- Open issue on GitHub repository (if applicable)

### ASPICE Process Questions
- Use the Q&A Chat feature in the tool
- Consult official ASPICE PAM documentation
- Seek guidance from certified ASPICE assessors
- Attend ASPICE training courses

### Custom Deployment
- Review [Programmatic API](#8-programmatic-api) section
- Check Python API documentation in source code
- Consider hiring consultant for enterprise deployment

---

## About This Manual

**Version**: 1.0  
**Last Updated**: 2024  
**Applicable to**: ASPICE Capability Checker v1.0+  
**Based on**: Automotive SPICE® v4.0, ISO/IEC 33020

This manual covers all features of the ASPICE Capability Checker agent and provides practical use cases for each capability. For the latest updates and additional resources, check the project repository.

---

**Note**: Automotive SPICE® is a registered trademark of VDA QMC. This tool is an independent implementation to support ASPICE process improvement and is not officially endorsed by VDA QMC or any standards organization.
