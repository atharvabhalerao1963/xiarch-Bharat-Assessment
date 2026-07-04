"""
cleaner.py

Cleans and normalizes extracted document content.
"""

import re

from models.schemas import SourceDocument
from utils.logger import logger


class DocumentCleaner:
    """
    Cleans extracted documents before further processing.
    """

    def clean(
        self,
        document: SourceDocument
    ) -> SourceDocument:

        logger.info(f"Cleaning document: {document.title}")

        text = document.content

        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text)

        # Remove repeated blank lines
        text = re.sub(r"\n+", "\n", text)

        text = text.strip()

        document.content = text

        return document

    def clean_documents(
        self,
        documents: list[SourceDocument]
    ) -> list[SourceDocument]:

        return [
            self.clean(doc)
            for doc in documents
        ]