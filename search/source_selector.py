"""
source_selector.py

Determines how the ResearchPlan should be executed.

The LLM decides WHAT categories of information should be searched.
This module decides WHICH search provider(s) should execute those
categories.
"""
from models.schemas import ResearchPlan, SearchTask
from utils.logger import logger


class SourceSelector:

    def create_search_tasks(
        self,
        plan: ResearchPlan
    ) -> list[SearchTask]:

        logger.info("Creating search tasks...")

        tasks = []

        for index, source in enumerate(plan.preferred_sources):

            keyword = plan.keywords[
                index % len(plan.keywords)
            ]

            search_query = f"{keyword} {source}"

            tasks.append(

                SearchTask(

                    provider="tavily",

                    query=search_query,

                    category=source,

                    max_results=plan.max_results

                )

            )

        logger.info(
            f"Created {len(tasks)} search task(s)."
        )

        return tasks