"""
context_builder.py

Builds the final context that will be sent to the LLM summarizer.
"""

from models.schemas import SourceDocument
from utils.logger import logger


class ContextBuilder:

    def build(
        self,
        documents: list[SourceDocument],
        max_documents: int = 8
    ) -> str:

        logger.info("Building research context...")

        selected = documents[:max_documents]

        sections = []

        for index, document in enumerate(selected, start=1):

            sections.append(

                f"""
DOCUMENT {index}

Title:
{document.title}

Source:
{document.url}

Content:
{document.content[:3500]}
"""

            )

        context = "\n\n".join(sections)

        logger.info(
            f"Context built using {len(selected)} document(s)."
        )

        return context