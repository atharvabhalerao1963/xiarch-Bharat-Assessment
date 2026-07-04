# 🤖 Autonomous Research Agent

An AI-powered autonomous research system that plans, searches, analyzes, and summarizes information from multiple external sources into a structured research report.

---

# 🚀 Quick Start

## 1. Clone the Repository

```bash
git clone https://github.com/atharvabhalerao1963/Autonomous-Research-Agent.git

cd Autonomous-Research-Agent
```

## 2. Create a Virtual Environment

### macOS / Linux

```bash
python -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

## 5. Run the Application

```bash
streamlit run app/ui.py
```

The application will be available at:

```
http://localhost:8501
```

---

# ✨ Features

* Autonomous research planning using Google Gemini
* Dynamic source selection based on the research topic
* Parallel web search across multiple external sources
* Intelligent content extraction using Trafilatura
* Duplicate removal and semantic relevance filtering
* AI-generated structured research reports
* Export reports as Markdown and PDF
* Local research history using SQLite
* Interactive Streamlit user interface

---

# 📌 Project Overview

The **Autonomous Research Agent** performs end-to-end research with minimal human intervention.

Instead of relying on predefined workflows or hardcoded responses, the system uses a Large Language Model (LLM) to understand the research objective, determine an appropriate search strategy, collect information from multiple sources, filter irrelevant content, and generate a structured report.

The project follows a modular architecture where every component has a single responsibility, making the system easier to maintain, test, and extend.

---

# 🏗️ System Architecture

```text
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

The research pipeline follows a sequential autonomous workflow:

1. User submits a research query.
2. Gemini creates a structured research plan.
3. The agent selects the most appropriate source categories.
4. Multiple searches are executed in parallel.
5. Web content is extracted and cleaned.
6. Duplicate documents are removed.
7. Semantic relevance filtering retains only useful information.
8. A unified research context is created.
9. Gemini generates a structured report.
10. The report is exported and stored in SQLite memory.

---

# 📂 Project Structure

```text
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

# 🛠️ Technology Stack

| Category           | Technology              |
| ------------------ | ----------------------- |
| Language           | Python                  |
| LLM                | Google Gemini 2.5 Flash |
| Search             | Tavily Search API       |
| Content Extraction | Trafilatura             |
| Semantic Filtering | Sentence Transformers   |
| Embedding Model    | all-MiniLM-L6-v2        |
| Database           | SQLite                  |
| UI                 | Streamlit               |
| Validation         | Pydantic                |
| PDF Generation     | ReportLab               |

---

# 💡 Key Design Decisions

### Why Gemini?

Gemini is responsible only for reasoning-intensive tasks such as research planning and structured report generation, ensuring efficient use of LLM resources.

### Why Semantic Filtering?

Semantic filtering is performed using sentence embeddings rather than repeated LLM calls. This significantly reduces latency, API usage, and operational cost while maintaining high-quality document selection.

### Why Parallel Search?

Executing multiple searches concurrently improves response time and increases the diversity of retrieved information.

### Why SQLite?

SQLite provides lightweight local persistence without requiring additional infrastructure, making it suitable for storing research history.

### Why Streamlit?

The project is designed as a standalone AI application. Streamlit offers a simple and interactive interface without the need for a separate backend API.

---

# 🔮 Future Improvements

Potential future enhancements include:

* Multi-agent collaboration
* Vector database integration
* Citation confidence scoring
* Streaming report generation
* REST API using FastAPI
* Docker support
* Cloud deployment
* Authentication and user management

---

# 👨‍💻 Author

**Atharva Bhalerao**

AI & ML Engineer | Data Science Enthusiast

**Xiarch Bharat – Autonomous Research Agent Assessment**
