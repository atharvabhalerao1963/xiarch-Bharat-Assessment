"""
ui.py

Streamlit User Interface for the Autonomous Research Agent.

Design Decisions
----------------
• Session State is used to preserve generated reports between reruns.
• The research pipeline executes only when the user clicks the button.
• Markdown and PDF exports are generated once per report.
• Download buttons use bytes instead of file handles to avoid Streamlit rerun issues.
• Layout uses a two-column shell (main content + right-hand info rail) instead of
  a heavy sidebar, for a more "product" feel than a default Streamlit demo.
"""
from datetime import datetime
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from memory.retrieval import MemoryRetriever
from app.main import AutonomousResearchAgent
from reports.markdown_export import MarkdownExporter
from reports.pdf_export import PDFExporter


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Autonomous Research Agent",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# Styling
# ============================================================
# Inline CSS is used here (instead of relying only on assets/styles.css) so the
# UI looks correct even if that file is missing, and so this file is fully
# self-contained / copy-paste-able.

BASE_CSS = """
<style>
    /* ---- Global ---- */
    .stApp {
        background: radial-gradient(circle at top left, #0f172a 0%, #0b1120 55%, #060a14 100%);
    }
    html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }

    #MainMenu, footer, header { visibility: hidden; }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* ---- Hero header ---- */
    .hero {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.75rem 2rem;
        border-radius: 18px;
        background: linear-gradient(135deg, rgba(59,130,246,0.18), rgba(139,92,246,0.12));
        border: 1px solid rgba(148,163,184,0.18);
        margin-bottom: 1.5rem;
    }
    .hero-title {
        font-size: 1.65rem;
        font-weight: 700;
        color: #f8fafc;
        margin: 0;
        letter-spacing: -0.02em;
    }
    .hero-subtitle {
        font-size: 0.92rem;
        color: #94a3b8;
        margin-top: 0.35rem;
    }
    .hero-badge {
        font-size: 0.75rem;
        font-weight: 600;
        color: #93c5fd;
        background: rgba(59,130,246,0.12);
        border: 1px solid rgba(59,130,246,0.35);
        padding: 0.35rem 0.85rem;
        border-radius: 999px;
        white-space: nowrap;
    }

    /* ---- Cards ---- */
    .panel {
        background: rgba(15, 23, 42, 0.55);
        border: 1px solid rgba(148,163,184,0.14);
        border-radius: 16px;
        padding: 1.4rem 1.5rem;
        margin-bottom: 1.1rem;
    }
    .panel h4 {
        color: #e2e8f0;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 0.6rem;
    }
    .feature-row {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        font-size: 0.87rem;
        color: #cbd5e1;
        padding: 0.3rem 0;
    }
    .feature-dot {
        color: #34d399;
        font-size: 0.8rem;
    }
    .stack-pill {
        display: inline-block;
        font-size: 0.75rem;
        color: #cbd5e1;
        background: rgba(148,163,184,0.10);
        border: 1px solid rgba(148,163,184,0.18);
        padding: 0.25rem 0.65rem;
        border-radius: 8px;
        margin: 0.2rem 0.3rem 0.2rem 0;
    }
    .history-item {
        font-size: 0.85rem;
        color: #cbd5e1;
        padding: 0.45rem 0;
        border-bottom: 1px dashed rgba(148,163,184,0.18);
    }
    .history-item:last-child { border-bottom: none; }

    /* ---- Inputs / buttons ---- */
    .stTextInput input {
        background: rgba(15,23,42,0.6);
        border: 1px solid rgba(148,163,184,0.25);
        color: #f1f5f9;
        border-radius: 10px;
        padding: 0.7rem 0.9rem;
    }
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
        border: none;
        background: linear-gradient(135deg, #3b82f6, #6366f1);
        color: white;
        padding: 0.65rem 1rem;
        transition: transform 0.15s ease;
    }
    .stButton button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(59,130,246,0.35);
    }
    .stDownloadButton button {
        border-radius: 10px;
        font-weight: 600;
        border: 1px solid rgba(148,163,184,0.3);
        background: rgba(15,23,42,0.5);
        color: #e2e8f0;
    }

    .report-container {
        background: rgba(15, 23, 42, 0.55);
        border: 1px solid rgba(148,163,184,0.14);
        border-radius: 16px;
        padding: 1.75rem 2rem;
    }

    .footer-caption {
        text-align: center;
        color: #64748b;
        font-size: 0.8rem;
        margin-top: 1.5rem;
    }
</style>
"""

st.markdown(BASE_CSS, unsafe_allow_html=True)

# Optional: still load an external stylesheet if present, appended after base CSS
css_path = PROJECT_ROOT / "assets" / "styles.css"
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# ============================================================
# Session State
# ============================================================

defaults = {
    "report": None,
    "query": "",
    "markdown_path": None,
    "pdf_path": None,
    "last_run_time": None,
    "error": None,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ============================================================
# Header
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div>
            <p class="hero-title">🔎 Autonomous Research Agent</p>
            <p class="hero-subtitle">
                Multi-source research, AI synthesis, and export-ready reports — in one query.
            </p>
        </div>
        <div class="hero-badge">Xiarch Bharat Assessment</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Main Layout — content column + info rail
# ============================================================

main_col, side_col = st.columns([2.3, 1], gap="large")

# ------------------------------------------------------------
# Main column: input, run, report
# ------------------------------------------------------------
with main_col:

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("#### Start a new research task")

    input_col, button_col = st.columns([4, 1], vertical_alignment="bottom")

    with input_col:
        query = st.text_input(
            "Research Topic",
            value=st.session_state.query,
            placeholder="e.g. Latest AI Regulations in Europe",
            label_visibility="collapsed",
        )

    with button_col:
        run_clicked = st.button("🚀 Run Research", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if run_clicked:
        if not query.strip():
            st.warning("Please enter a research topic before starting.")
        else:
            st.session_state.query = query
            st.session_state.error = None

            try:
                with st.spinner("Planning, searching, and synthesizing your report..."):
                    agent = AutonomousResearchAgent()
                    report = agent.run(query)

                    markdown_exporter = MarkdownExporter()
                    markdown_path = markdown_exporter.export(report)

                    pdf_exporter = PDFExporter()
                    pdf_path = pdf_exporter.export(report)

                    st.session_state.report = report
                    st.session_state.markdown_path = markdown_path
                    st.session_state.pdf_path = pdf_path
                    st.session_state.last_run_time = datetime.now().strftime("%d %b %Y, %I:%M %p")

                st.success("Research completed successfully.")

            except Exception as exc:
                st.session_state.error = str(exc)
                st.error(f"Research failed: {exc}")

    # --------------------------------------------------------
    # Report display
    # --------------------------------------------------------
    if st.session_state.report:

        meta_col1, meta_col2 = st.columns([3, 1])
        with meta_col1:
            st.markdown(f"#### 📑 Research Report — *{st.session_state.query}*")
        with meta_col2:
            if st.session_state.last_run_time:
                st.caption(f"Generated: {st.session_state.last_run_time}")

        st.markdown('<div class="report-container">', unsafe_allow_html=True)
        st.markdown(st.session_state.report)
        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")
        dl_col1, dl_col2 = st.columns(2)

        with dl_col1:
            markdown_bytes = Path(st.session_state.markdown_path).read_bytes()
            st.download_button(
                label="⬇ Download Markdown",
                data=markdown_bytes,
                file_name="research_report.md",
                mime="text/markdown",
                use_container_width=True,
            )

        with dl_col2:
            pdf_bytes = Path(st.session_state.pdf_path).read_bytes()
            st.download_button(
                label="⬇ Download PDF",
                data=pdf_bytes,
                file_name="research_report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.info("Enter a topic above and click **Run Research** to generate your first report.")

# ------------------------------------------------------------
# Right rail: features, tech stack, history
# ------------------------------------------------------------
with side_col:

    st.markdown(
        """
        <div class="panel">
            <h4>Capabilities</h4>
            <div class="feature-row"><span class="feature-dot">●</span> Autonomous planning</div>
            <div class="feature-row"><span class="feature-dot">●</span> Parallel web search</div>
            <div class="feature-row"><span class="feature-dot">●</span> Semantic filtering</div>
            <div class="feature-row"><span class="feature-dot">●</span> AI summarization</div>
            <div class="feature-row"><span class="feature-dot">●</span> PDF &amp; Markdown export</div>
            <div class="feature-row"><span class="feature-dot">●</span> SQLite-backed memory</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="panel">
            <h4>Tech Stack</h4>
            <span class="stack-pill">Gemini 2.5 Flash</span>
            <span class="stack-pill">Tavily Search API</span>
            <span class="stack-pill">Sentence Transformers</span>
            <span class="stack-pill">Trafilatura</span>
            <span class="stack-pill">SQLite</span>
            <span class="stack-pill">Streamlit</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    retriever = MemoryRetriever()
    history = retriever.get_history()

    history_html = '<div class="panel"><h4>📚 Previous Searches</h4>'
    if history:
        for item in history[:10]:
            history_html += f'<div class="history-item">{item[1]}</div>'
    else:
        history_html += '<div class="history-item">No searches yet.</div>'
    history_html += "</div>"

    st.markdown(history_html, unsafe_allow_html=True)

# ============================================================
# Footer
# ============================================================

st.markdown(
    '<p class="footer-caption">Built by Atharva Bhalerao • Autonomous Research Agent • Xiarch Bharat Assessment</p>',
    unsafe_allow_html=True,
)