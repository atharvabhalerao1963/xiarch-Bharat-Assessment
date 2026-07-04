"""
retrieval.py

Retrieves previously stored research reports.
"""

import sqlite3

from memory.database import MemoryDatabase


class MemoryRetriever:

    def __init__(self):

        self.database = MemoryDatabase()

    def get_history(self):

        connection = sqlite3.connect(
            self.database.database_path
        )

        cursor = connection.cursor()

        cursor.execute(

            """
            SELECT

                id,
                query,
                created_at

            FROM research_history

            ORDER BY created_at DESC
            """

        )

        rows = cursor.fetchall()

        connection.close()

        return rows

    def get_report(

        self,

        report_id: int

    ):

        connection = sqlite3.connect(
            self.database.database_path
        )

        cursor = connection.cursor()

        cursor.execute(

            """
            SELECT report

            FROM research_history

            WHERE id=?
            """,

            (
                report_id,
            )

        )

        row = cursor.fetchone()

        connection.close()

        if row:

            return row[0]

        return None