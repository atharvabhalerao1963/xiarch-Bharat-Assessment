"""

Purpose
-------
This module performs semantic relevance filtering using sentence embeddings.

Why embeddings instead of an LLM?
---------------------------------
Although an LLM could classify every document individually, that would require
one API request per document, making the system slower, more expensive, and
subject to API rate limits.

Instead, we use semantic embeddings to measure how closely each document
matches the user's query.
Benefits -:

Faster
More scalable 
Lower cost
Better suited for retrieval tasks

The LLM is then used only where reasoning is actually required:
    - Research Planning
    - Final Research Summarization
    - Actionable Insight Generation
"""

from sentence_transformers import SentenceTransformer, util

from models.schemas import SourceDocument
from utils.logger import logger


class RelevanceFilter:
    """
    Filters documents based on semantic similarity between the
    user's query and the extracted document content.
    """

    def __init__(self):

        logger.info("Loading embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def filter_documents(
        self,
        query: str,
        documents: list[SourceDocument],
        threshold: float = 0.40,
        top_k: int = 8
    ) -> list[SourceDocument]:

        logger.info("Calculating semantic similarity...")

        if not documents:
            return []

        query_embedding = self.model.encode(
            query,
            convert_to_tensor=True
        )

        scored_documents = []

        for document in documents:

            document_embedding = self.model.encode(
                document.content[:2000],
                convert_to_tensor=True
            )

            similarity = util.cos_sim(
                query_embedding,
                document_embedding
            ).item()

            logger.info(
                f"{document.title[:60]} -> {similarity:.3f}"
            )

            if similarity >= threshold:

                scored_documents.append(
                    (similarity, document)
                )

        scored_documents.sort(
            key=lambda x: x[0],
            reverse=True
        )

        selected_documents = [
            document
            for _, document in scored_documents[:top_k]
        ]

        logger.info(
            f"Selected {len(selected_documents)} highly relevant document(s)."
        )

        return selected_documents