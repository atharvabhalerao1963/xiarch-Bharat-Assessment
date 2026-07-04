"""
database.py

Creates and manages the SQLite database used for storing
previous research sessions.

Design Decision
---------------
SQLite was selected because it is:

• Lightweight
• Serverless
• Portable
• Suitable for local AI agents

Each research session stores:

- User Query
- Generated Report
- Timestamp
"""

import sqlite3
from pathlib import Path

from utils.logger import logger


class MemoryDatabase:

    def __init__(
        self,
        database_path: str = "memory/research_history.db"
    ):

        self.database_path = database_path

        Path("memory").mkdir(
            exist_ok=True
        )

        self.initialize_database()

    def initialize_database(self):

        logger.info(
            "Initializing research history database..."
        )

        connection = sqlite3.connect(
            self.database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS research_history (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                query TEXT NOT NULL,

                report TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        connection.commit()

        connection.close()

        logger.info(
            "Database initialized successfully."
        )