"""
markdown_export.py

Exports the formatted research report as a Markdown file.

Design Decision
---------------
The exporter receives an already formatted report string.

It has no knowledge of:

- Gemini
- Search
- Embeddings
- ResearchReport

This keeps responsibilities separated and makes the
exporter reusable.
"""

from pathlib import Path

from utils.logger import logger


class MarkdownExporter:

    def export(
        self,
        report: str,
        filename: str = "research_report.md",
        output_dir: str = "exports"
    ) -> Path:

        logger.info("Exporting Markdown report...")

        output_path = Path(output_dir)

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = output_path / filename

        file_path.write_text(
            report,
            encoding="utf-8"
        )

        logger.info(
            f"Markdown report saved to {file_path}"
        )

        return file_path