"""
client.py

Reusable Gemini client for the Autonomous Research Agent.

This module is the ONLY place that communicates directly with
the Gemini API. Every AI-powered module (Planner, Summarizer,
Insight Generator) will use this client.
"""


from google import genai
from google.genai import types

from app.config import settings
from utils.logger import logger


class GeminiClient:
    """
    Wrapper around the Gemini API.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model = settings.llm_model

    def generate_text(self, prompt: str) -> str:
        """
        Generate a plain text response.
        """

        logger.info("Sending text request to Gemini...")

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        logger.info("Text response received.")

        return response.text

    def generate_structured(self, prompt: str, schema):
        """
        Generate a structured response using a Pydantic schema.
        """

        logger.info("Sending structured request to Gemini...")

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=schema,
            ),
        )

        logger.info("Structured response received.")

        return response.parsed