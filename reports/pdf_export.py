"""
pdf_export.py

Exports the formatted research report as a PDF.

Design Decision
---------------
This module only handles PDF generation.

It receives a formatted report string and converts it into
a PDF document.

The exporter is completely independent of the LLM,
search engine, and formatter.
"""

from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

from utils.logger import logger


class PDFExporter:

    def export(
        self,
        report: str,
        filename: str = "research_report.pdf",
        output_dir: str = "exports"
    ) -> Path:

        logger.info("Exporting PDF report...")

        output_path = Path(output_dir)

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = output_path / filename

        document = SimpleDocTemplate(
            str(file_path)
        )

        styles = getSampleStyleSheet()

        story = []

        # Preserve blank lines
        for line in report.split("\n"):

            if line.strip():

                story.append(
                    Paragraph(line.replace(" ", "&nbsp;"), styles["BodyText"])
                )

            else:

                story.append(
                    Paragraph("<br/>", styles["BodyText"])
                )

        document.build(story)

        logger.info(
            f"PDF report saved to {file_path}"
        )

        return file_path