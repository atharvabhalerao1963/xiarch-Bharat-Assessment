"""
summarizer.py

Uses Gemini to generate the final structured research report.
"""

from llm.client import GeminiClient
from llm.prompts import SUMMARY_PROMPT
from models.schemas import ResearchReport
from utils.logger import logger


class ResearchSummarizer:

    def __init__(self):

        self.llm = GeminiClient()

    def summarize(
        self,
        query: str,
        context: str
    ) -> ResearchReport:

        logger.info("Generating final research report...")

        prompt = SUMMARY_PROMPT.format(
            query=query,
            context=context
        )

        report = self.llm.generate_structured(
            prompt=prompt,
            schema=ResearchReport
        )

        logger.info("Research report generated successfully.")

        return report