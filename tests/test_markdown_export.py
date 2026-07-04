# run : python test_markdown_export.py
from reports.markdown_export import MarkdownExporter

from reports.formatter import ReportFormatter

# Reuse the report object from your summarizer test.

formatted_report = formatter.format(report)

exporter = MarkdownExporter()

path = exporter.export(
    formatted_report
)

print()

print(f"Markdown saved to: {path}")