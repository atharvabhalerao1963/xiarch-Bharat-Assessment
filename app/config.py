"""
This file centralizes all the application's configuration. Instead of hardcoding values like API keys,
debug mode, or application settings throughout the project, everything is loaded from the .env file and 
accessed through a single settings object. This is used makes the application secure, maintainable, and easy to 
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
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")

        # Research Settings
        self.max_search_results = int(
            os.getenv("MAX_SEARCH_RESULTS", 5)
        )

        # Export Settings
        self.export_folder = os.getenv(
            "EXPORT_FOLDER",
            "exports"
        )



settings = Settings() # It creates one global instance of the Settings class.