"""
deduplicator.py

Removes duplicate documents based on URL.
"""

from models.schemas import SourceDocument
from utils.logger import logger


class DocumentDeduplicator:

    def remove_duplicates(
        self,
        documents: list[SourceDocument]
    ) -> list[SourceDocument]:

        logger.info("Removing duplicate documents...")

        unique = {}
        
        for document in documents:
            unique[str(document.url)] = document

        cleaned = list(unique.values())

        logger.info(
            f"Removed {len(documents) - len(cleaned)} duplicate document(s)."
        )

        return cleaned