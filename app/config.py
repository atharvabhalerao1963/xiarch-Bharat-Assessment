"""
This file centralizes all the application's configuration. Instead of hardcoding values like API keys,
debug mode, or application settings throughout the project, everything is loaded from the .env file and
accessed through a single settings object. This makes the application secure, maintainable, and easy to
configure for different environments.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """
    Application configuration settings.
    """

    def __init__(self):
        # Application Settings
        self.app_name = os.getenv("APP_NAME", "Autonomous Research Agent")
        self.debug = os.getenv("DEBUG", "False").lower() == "true"

        # API Keys
        self.tavily_api_key = os.getenv("TAVILY_API_KEY", "")
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")

        # LLM Configuration
        self.llm_provider = os.getenv("LLM_PROVIDER", "gemini")
        self.llm_model = os.getenv("LLM_MODEL", "gemini-2.5-flash")

        # Research Settings
        self.max_search_results = int(
            os.getenv("MAX_SEARCH_RESULTS", 5)
        )

        # Export Settings
        self.export_folder = os.getenv(
            "EXPORT_FOLDER",
            "exports"
        )

        # tavily_api_key
        self.tavily_api_key = os.getenv(
         "TAVILY_API_KEY","")


# Singleton settings object
settings = Settings()