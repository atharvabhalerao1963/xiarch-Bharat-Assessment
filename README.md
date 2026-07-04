# 🤖 Autonomous Research Agent

> **Xiarch Bharat – Assessment Option 1**

An AI-powered Autonomous Research Agent that automatically plans research, gathers information from multiple external sources, extracts and filters relevant content, and generates a structured research report with actionable insights.

---

# 📌 Project Overview

The Autonomous Research Agent is designed to perform end-to-end research on any user-provided topic with minimal human intervention.

Instead of relying on hardcoded rules or predefined responses, the system uses a Large Language Model (LLM) to autonomously:

- Understand the user's research objective
- Create a research plan
- Select appropriate information sources
- Search multiple external resources
- Extract article content
- Remove duplicate and irrelevant information
- Generate a structured research report
- Export reports in Markdown and PDF
- Store previous research history

The project follows a modular architecture where every component has a single responsibility, making the system scalable, maintainable, and easy to extend.

---

# 🎯 Assignment Requirements

| Requirement | Status |
|------------|--------|
| Accept User Query | ✅ |
| Search External Sources | ✅ |
| Extract Relevant Information | ✅ |
| Remove Duplicate Content | ✅ |
| Remove Irrelevant Content | ✅ |
| Generate Structured Summary | ✅ |
| Key Points | ✅ |
| Important Findings | ✅ |
| References | ✅ |
| Actionable Insights | ✅ |

---

# ⭐ Bonus Features

- ✅ Autonomous source selection using Gemini
- ✅ Parallel web search
- ✅ Markdown export
- ✅ PDF export
- ✅ SQLite-based research history
- ✅ Streamlit user interface

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
              Streamlit Interface
                      │
                      ▼
        Autonomous Research Agent
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Research       Parallel Search     Memory
 Planner             │             (SQLite)
(Gemini)             ▼
              Content Extraction
                      ▼
               Document Cleaning
                      ▼
            Duplicate Removal
                      ▼
        Semantic Relevance Filtering
                      ▼
              Context Builder
                      ▼
            Gemini Summarizer
                      ▼
            Report Formatter
                      ▼
        PDF / Markdown Export
```

---

# ⚙️ Workflow

### Step 1 – User Query

The user enters a research topic through the Streamlit interface.

Example:

```
Latest AI Regulations in Europe
```

---

### Step 2 – Autonomous Planning

Gemini analyzes the query and automatically creates a structured research plan.

The planner identifies:

- User intent
- Keywords
- Search strategy
- Preferred sources
- Number of search results

---

### Step 3 – Source Selection

Based on the research plan, the agent determines appropriate external sources instead of using predefined websites.

Examples include:

- Government websites
- Official documentation
- Academic sources
- Trusted news platforms

---

### Step 4 – Parallel Information Gathering

Multiple search tasks are executed concurrently to improve research speed and source diversity.

---

### Step 5 – Content Extraction

Each webpage is downloaded and processed using Trafilatura to extract the primary textual content.

---

### Step 6 – Data Processing

The extracted documents undergo several processing stages:

- Cleaning
- Duplicate removal
- Semantic relevance filtering

Semantic filtering is implemented using sentence embeddings instead of repeated LLM calls to improve efficiency, reduce API usage, and increase scalability.

---

### Step 7 – Context Building

Relevant documents are merged into a unified research context while preserving useful information from multiple sources.

---

### Step 8 – AI Summarization

Gemini generates a structured report containing:

- Executive Summary
- Key Points
- Important Findings
- References
- Actionable Insights
- Limitations

---

### Step 9 – Report Generation

The report can be exported as:

- Markdown
- PDF

---

### Step 10 – Memory

Each completed research report is stored inside a local SQLite database, allowing previous searches to be retrieved later.

---

# 📂 Project Structure

```
Autonomous-Research-Agent/

├── agent/
├── app/
├── assets/
├── extraction/
├── llm/
├── memory/
├── models/
├── processing/
├── reports/
├── search/
├── tests/
├── utils/

├── exports/

├── README.md
├── requirements.txt
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## LLM

- Google Gemini 2.5 Flash

## Search

- Tavily Search API

## Content Extraction

- Trafilatura

## Semantic Search

- Sentence Transformers
- all-MiniLM-L6-v2

## Database

- SQLite

## User Interface

- Streamlit

## Data Validation

- Pydantic

## PDF Generation

- ReportLab

---

# 💡 Design Decisions

## Why Gemini?

Gemini is used for reasoning-intensive tasks such as research planning and structured report generation because it provides reliable structured outputs and strong reasoning capabilities.

---

## Why Tavily?

Tavily is optimized for AI agents and returns high-quality search results with metadata, making it well suited for autonomous research workflows.

---

## Why Semantic Filtering instead of LLM Filtering?

Initially, relevance filtering was performed using Gemini.

However, repeated LLM calls significantly increased latency and API usage.

The implementation was redesigned to use sentence embeddings, allowing semantic similarity calculations locally.

Benefits include:

- Faster execution
- Lower API cost
- Better scalability
- Reduced dependency on LLM quota

The LLM is therefore reserved only for high-level reasoning tasks.

---

## Why SQLite?

SQLite provides lightweight local persistence without requiring any external database server.

It is sufficient for storing research history and keeps the project self-contained.

---

## Why Streamlit?

The project is designed as a standalone AI application.

Since no REST API was required by the assignment, Streamlit provides a simpler and more user-friendly interface than introducing an additional FastAPI layer.

---

# 🚀 Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Autonomous-Research-Agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

---

# ▶️ Running the Application

```bash
python -m streamlit run app/ui.py
```

---

# 📸 Sample Output

The application generates a structured report containing:

- Executive Summary
- Key Points
- Findings
- References
- Actionable Insights

The report can be downloaded in Markdown and PDF formats.

---

# 🔮 Future Improvements

Possible future enhancements include:

- Multi-agent research collaboration
- Vector database integration
- Live web crawling
- Citation confidence scoring
- Interactive report editing
- REST API support
- Cloud deployment

---

# 👨‍💻 Author

**Atharva Bhalerao**

AI & ML Engineer | Data Science Enthusiast

Xiarch Bharat Assessment Submission