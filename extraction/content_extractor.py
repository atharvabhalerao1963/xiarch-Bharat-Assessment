"""
This module is responsible for downloading a webpage from a search result and extracting its main textual
 content using Trafilatura. If the webpage is successfully processed, it creates a validated SourceDocument 
 object. If downloading or extraction fails, it returns None so the workflow can safely skip that document
   instead of crashing
"""

import trafilatura

from models.schemas import SearchResult
from models.schemas import SourceDocument

from utils.logger import logger


class ContentExtractor:

    def extract(
        self,
        result: SearchResult  # parameter must be a SearchResult object.
    ) -> SourceDocument | None:  

        logger.info(
            f"Extracting: {result.url}"
        )

        downloaded = trafilatura.fetch_url(
            str(result.url)
        )

        if not downloaded:

            logger.warning(
                "Failed to download page."
            )

            return None

        text = trafilatura.extract(
            downloaded
        )

        if not text:

            logger.warning(
                "No article text extracted."
            )

            return None

        return SourceDocument(

            title=result.title,

            url=str(result.url),

            content=text,

            source=result.source
        )