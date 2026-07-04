"""
main.py

Main application controller.

This module orchestrates the complete autonomous
research workflow.

Design Decision
---------------
All pipeline logic is centralized here.

Benefits
--------
• Single entry point
• Easy UI integration
• Easy testing
• No duplicated workflow
"""

import asyncio

from agent.planner import ResearchPlanner

from extraction.content_extractor import ContentExtractor

from llm.summarizer import ResearchSummarizer

from memory.history import HistoryManager

from models.schemas import UserQuery

from processing.cleaner import DocumentCleaner
from processing.context_builder import ContextBuilder
from processing.deduplicator import DocumentDeduplicator
from processing.relevance_filter import RelevanceFilter

from reports.formatter import ReportFormatter

from search.parallel_search import ParallelSearcher
from search.source_selector import SourceSelector


class AutonomousResearchAgent:

    def __init__(self):

        self.planner = ResearchPlanner()

        self.selector = SourceSelector()

        self.parallel = ParallelSearcher()

        self.extractor = ContentExtractor()

        self.cleaner = DocumentCleaner()

        self.deduplicator = DocumentDeduplicator()

        self.filterer = RelevanceFilter()

        self.builder = ContextBuilder()

        self.summarizer = ResearchSummarizer()

        self.formatter = ReportFormatter()

        self.memory = HistoryManager()

    def run(
        self,
        query: str
    ) -> str:

        user_query = UserQuery(
            query=query
        )


        plan = self.planner.create_plan(
            user_query
        )

       
        tasks = self.selector.create_search_tasks(
            plan
        )


        results = asyncio.run(
            self.parallel.search(tasks)
        )


        documents = []

        for result in results:

            document = self.extractor.extract(result)

            if document:
                documents.append(document)


        documents = self.cleaner.clean_documents(
            documents
        )


        documents = self.deduplicator.remove_duplicates(
            documents
        )


        documents = self.filterer.filter_documents(
            query=query,
            documents=documents,
            top_k=8
        )


        context = self.builder.build(
            documents
        )


        report = self.summarizer.summarize(
            query=query,
            context=context
        )


        formatted_report = self.formatter.format(
            report
        )


        self.memory.save_report(
            query=query,
            report=formatted_report
        )

        return formatted_report