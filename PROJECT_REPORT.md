# Project Report
## Autonomous Research Agent

**Assessment:** Xiarch Bharat – Assessment Option 1

**Developer:** Atharva Bhalerao

---

# 1. Project Overview

The Autonomous Research Agent is an AI-powered application designed to automate the complete research workflow. Given a user-defined topic, the system autonomously plans the research strategy, searches multiple external sources, extracts relevant information, removes duplicate and low-quality content, and generates a structured research report containing key findings, references, and actionable insights.

Unlike traditional search applications that simply return links, this system performs reasoning, information aggregation, and report generation using a Large Language Model while minimizing unnecessary LLM usage through semantic filtering techniques.

The application has been designed with modularity, maintainability, and scalability as primary goals.

---

# 2. Project Objectives

The main objectives of the project were:

- Build an autonomous research workflow.
- Accept natural language research queries.
- Search multiple external sources dynamically.
- Extract useful textual information from webpages.
- Remove duplicate and irrelevant information.
- Generate a structured AI-powered report.
- Export reports as Markdown and PDF.
- Maintain previous research history locally.

---

# 3. High-Level Workflow

The application follows the following sequence:

```

User Query
↓
Research Planning (Gemini)
↓
Source Selection
↓
Parallel Web Search
↓
Content Extraction
↓
Document Cleaning
↓
Duplicate Removal
↓
Semantic Relevance Filtering
↓
Context Building
↓
AI Summarization
↓
Report Formatting
↓
Markdown / PDF Export
↓
SQLite History

```

Each stage is implemented as an independent module to improve maintainability and simplify future extensions.

---

# 4. System Architecture

The project follows a modular architecture where every module has a clearly defined responsibility.

### Planning Layer

Responsible for understanding the user's research objective and creating a structured research plan using Gemini.

### Search Layer

Uses Tavily Search API to retrieve information from multiple external sources.

Parallel search execution reduces the overall response time.

### Extraction Layer

Downloads webpages and extracts meaningful textual content using Trafilatura.

Navigation elements, advertisements, and unnecessary HTML content are discarded automatically.

### Processing Layer

The extracted content undergoes several processing stages:

- Document Cleaning
- Duplicate Removal
- Semantic Relevance Filtering
- Context Building

This produces a high-quality research context for the LLM.

### AI Layer

Gemini generates a structured report containing:

- Executive Summary
- Key Points
- Important Findings
- References
- Actionable Insights
- Limitations

### Reporting Layer

The structured report is converted into a clean Markdown document and exported as both Markdown and PDF.

### Memory Layer

Every completed research report is stored locally using SQLite, allowing previous research sessions to be retrieved later.

---

# 5. Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| User Interface | Streamlit |
| LLM | Google Gemini 2.5 Flash |
| Search Engine | Tavily API |
| Content Extraction | Trafilatura |
| Semantic Search | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Database | SQLite |
| Data Validation | Pydantic |
| PDF Generation | ReportLab |

---

# 6. Important Engineering Decisions

## LLM for Reasoning Only

The Large Language Model is used only for tasks requiring reasoning:

- Research Planning
- Structured Report Generation

This reduces unnecessary API usage while preserving high-quality outputs.

---

## Semantic Relevance Filtering

Initially, relevance filtering was implemented using repeated LLM calls.

This approach increased execution time and API cost.

The implementation was redesigned to use Sentence Transformers and cosine similarity for semantic filtering.

Benefits:

- Lower API usage
- Faster execution
- Improved scalability
- Consistent filtering quality

This decision significantly reduced dependence on external LLM calls.

---

## Parallel Search

Instead of searching sources sequentially, multiple search tasks are executed concurrently.

Advantages:

- Faster research completion
- Better source diversity
- Improved overall throughput

---

## SQLite Memory

SQLite was selected because it provides a lightweight local database without requiring additional infrastructure.

For the assessment requirements, this was sufficient while keeping deployment simple.

---

# 7. Challenges Faced

Several challenges were encountered during development:

- Parsing inconsistent webpage structures.
- Handling duplicate search results from different sources.
- Reducing unnecessary LLM calls.
- Managing Gemini API rate limits.
- Designing a modular architecture instead of tightly coupled scripts.
- Maintaining clean separation between data processing and presentation.

Each issue resulted in improvements to the overall system design.

---

# 8. Performance

Typical execution time:

**30–40 seconds**

The execution time varies depending on:

- Search API response time
- Webpage download speed
- Number of retrieved documents
- Gemini response latency

Parallel search considerably reduces the overall research time.

---

# 9. Current Limitations

The current implementation has several known limitations.

- Performance depends on external APIs.
- Research speed depends on internet connectivity.
- Public web sources may occasionally contain outdated information.
- Semantic filtering cannot completely eliminate partially relevant documents.
- SQLite is intended for single-user usage.

These limitations are acceptable for the scope of the current assessment.

---

# 10. Future Improvements

Possible future enhancements include:

- Multi-agent collaboration
- Vector database memory
- Incremental document indexing
- Streaming report generation
- Source credibility scoring
- Citation confidence metrics
- REST API using FastAPI
- Docker deployment
- Cloud hosting
- Authentication and user accounts

---

# 11. Development Transparency

This project was independently designed and implemented as part of the Xiarch Bharat assessment.

During development, ChatGPT was used as an engineering assistant for discussing architecture, debugging specific implementation issues, refactoring portions of the codebase, and improving documentation.

All architectural decisions, module integration, implementation, testing, validation, and final verification were performed and reviewed by the developer.

---

# 12. Conclusion

The Autonomous Research Agent successfully fulfills all mandatory requirements of the assessment while also implementing every optional bonus feature.

The project demonstrates the use of Large Language Models within a modular software architecture rather than treating the LLM as the entire application. By combining autonomous planning, parallel information gathering, semantic document filtering, structured report generation, and local memory, the system provides an end-to-end research workflow that is scalable, maintainable, and practical.

The project also emphasizes clean software engineering principles, including modular design, separation of concerns, reusable components, and transparent documentation, making it suitable for future enhancements and production-oriented development.