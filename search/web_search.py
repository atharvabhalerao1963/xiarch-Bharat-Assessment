"""
web_search.py

Handles communication with the Tavily Search API.
"""

from tavily import TavilyClient

from app.config import settings
from models.schemas import SearchResult
from models.schemas import SearchTask
from utils.logger import logger


class TavilySearch:

    def __init__(self):

        self.client = TavilyClient(
            api_key=settings.tavily_api_key
        )

    def search(
        self,
        task: SearchTask
    ) -> list[SearchResult]:

        logger.info(
            f"Searching: {task.category}"
        )

        response = self.client.search(
            query=task.category,
            max_results=task.max_results,
            search_depth="advanced"
        )

        results = []

        for item in response.get("results", []):

            results.append(

                SearchResult(

                    title=item.get("title", ""),

                    url=item.get("url", ""),

                    snippet=item.get("content", ""),

                    source="Tavily"
                )

            )

        logger.info(
            f"Retrieved {len(results)} results."
        )

        return results