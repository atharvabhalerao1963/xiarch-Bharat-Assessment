"""
history.py

Stores completed research reports inside SQLite.
"""

import sqlite3

from memory.database import MemoryDatabase
from utils.logger import logger


class HistoryManager:

    def __init__(self):

        self.database = MemoryDatabase()

    def save_report(

        self,

        query: str,

        report: str

    ):

        logger.info(
            "Saving research report..."
        )

        connection = sqlite3.connect(
            self.database.database_path
        )

        cursor = connection.cursor()

        cursor.execute(

            """
            INSERT INTO research_history
            (
                query,
                report
            )

            VALUES (?, ?)
            """,

            (
                query,
                report
            )

        )

        connection.commit()

        connection.close()

        logger.info(
            "Research report saved."
        )