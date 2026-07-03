"""
parallel_search.py

Runs multiple search tasks concurrently.
"""

import asyncio

from models.schemas import SearchResult
from models.schemas import SearchTask

from search.web_search import TavilySearch

from utils.logger import logger


class ParallelSearcher:

    def __init__(self):

        self.searcher = TavilySearch()

    async def _run_task(
        self,
        task: SearchTask
    ):

        return await asyncio.to_thread(
            self.searcher.search,
            task
        )

    async def search(
        self,
        tasks: list[SearchTask]
    ) -> list[SearchResult]:

        logger.info(
            f"Running {len(tasks)} search tasks in parallel..."
        )

        results = await asyncio.gather(
            *[
                self._run_task(task)
                for task in tasks
            ]
        )

        merged = []

        for group in results:

            merged.extend(group)

        logger.info(
            f"Collected {len(merged)} search results."
        )

        return merged