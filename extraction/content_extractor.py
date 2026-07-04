"""
content_extractor.py

Downloads webpages from search results and extracts the main textual
content using Trafilatura.

If extraction is successful, a validated SourceDocument object is
returned. If downloading or extraction fails, None is returned so
the workflow can safely continue processing other documents.
"""

import trafilatura

from models.schemas import SearchResult, SourceDocument
from utils.logger import logger


class ContentExtractor:
    """
    Downloads and extracts clean text from webpages.
    """

    def extract(
        self,
        result: SearchResult
    ) -> SourceDocument | None:
        """
        Extract the main textual content from a webpage.

        Args:
            result: A SearchResult object containing the webpage URL.

        Returns:
            A SourceDocument if extraction succeeds, otherwise None.
        """

        logger.info(f"Extracting: {result.url}")

        try:
            # Download webpage
            downloaded = trafilatura.fetch_url(str(result.url))

            if not downloaded:
                logger.warning(f"Failed to download page: {result.url}")
                return None

            # Extract readable content
            text = trafilatura.extract(downloaded)

            if not text:
                logger.warning(f"No article text extracted from: {result.url}")
                return None

            # Create SourceDocument
            return SourceDocument(
                title=result.title,
                url=str(result.url),
                snippet=result.snippet,
                content=text,
                source=result.source,
            )

        except Exception as error:
            logger.error(f"Content extraction failed: {error}")
            return None