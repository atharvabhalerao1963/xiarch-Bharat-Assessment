"""
planner.py

This module is responsible for creating a structured research plan from the user's query.
It acts as the planning component of the autonomous agent. It sends the user's query to
the Gemini LLM, receives the response, converts it into a structured ResearchPlan object,
validates it using Pydantic, and returns it for the rest of the workflow.
"""

from llm.client import GeminiClient
from llm.prompts import PLANNER_PROMPT

from models.schemas import (
    UserQuery,
    ResearchPlan,
)

from utils.logger import logger


class ResearchPlanner:
    """
    Uses Gemini to generate a structured research plan.
    """

    def __init__(self):
        """
        Initialize the Gemini client.
        """
        self.llm = GeminiClient()

    def create_plan(
        self,
        user_query: UserQuery
    ) -> ResearchPlan:
        """
        Generate a structured research plan using Gemini.

        Args:
            user_query: User's research query.

        Returns:
            Validated ResearchPlan object.
        """

        logger.info("Generating research plan...")

        prompt = PLANNER_PROMPT.format(
            query=user_query.query
        )

        plan = self.llm.generate_structured(
            prompt=prompt,
            schema=ResearchPlan
        )

        logger.info("Research plan created successfully.")

        return plan