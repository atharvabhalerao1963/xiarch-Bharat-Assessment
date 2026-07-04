"""
test_summarizer.py

Tests the complete research pipeline up to the final
LLM-generated research report.
"""

import asyncio

from agent.planner import ResearchPlanner
from extraction.content_extractor import ContentExtractor

from llm.summarizer import ResearchSummarizer

from models.schemas import UserQuery

from processing.cleaner import DocumentCleaner
from processing.context_builder import ContextBuilder
from processing.deduplicator import DocumentDeduplicator
from processing.relevance_filter import RelevanceFilter

from search.parallel_search import ParallelSearcher
from search.source_selector import SourceSelector


# ============================================================
# Initialize Components
# ============================================================

planner = ResearchPlanner()

selector = SourceSelector()

parallel = ParallelSearcher()

extractor = ContentExtractor()

cleaner = DocumentCleaner()

deduplicator = DocumentDeduplicator()

filterer = RelevanceFilter()

builder = ContextBuilder()

summarizer = ResearchSummarizer()


# ============================================================
# User Query
# ============================================================

query = UserQuery(
    query="Latest AI Regulations in Europe"
)


# ============================================================
# Step 1 : Create Research Plan
# ============================================================

plan = planner.create_plan(query)


# ============================================================
# Step 2 : Create Search Tasks
# ============================================================

tasks = selector.create_search_tasks(plan)


# ============================================================
# Step 3 : Parallel Search
# ============================================================

results = asyncio.run(
    parallel.search(tasks)
)


# ============================================================
# Step 4 : Extract Documents
# ============================================================

documents = []

for result in results:

    document = extractor.extract(result)

    if document:

        documents.append(document)


print(f"\nExtracted Documents : {len(documents)}")


# ============================================================
# Step 5 : Clean Documents
# ============================================================

documents = cleaner.clean_documents(
    documents
)


# ============================================================
# Step 6 : Remove Duplicates
# ============================================================

documents = deduplicator.remove_duplicates(
    documents
)


# ============================================================
# Step 7 : Semantic Relevance Filtering
# ============================================================

documents = filterer.filter_documents(

    query=query.query,

    documents=documents,

    top_k=8

)


print(f"Relevant Documents : {len(documents)}")


# ============================================================
# Step 8 : Build Context
# ============================================================

context = builder.build(
    documents
)


print(f"Context Length : {len(context)} characters")


# ============================================================
# Step 9 : Generate Final Research Report
# ============================================================

report = summarizer.summarize(

    query=query.query,

    context=context

)


# ============================================================
# Display Report
# ============================================================

print("\n")
print("=" * 100)
print("FINAL RESEARCH REPORT")
print("=" * 100)


print("\n")
print("EXECUTIVE SUMMARY")
print("-" * 100)
print(report.executive_summary)


print("\n")
print("KEY POINTS")
print("-" * 100)

for index, point in enumerate(report.key_points, start=1):

    print(f"{index}. {point}")


print("\n")
print("IMPORTANT FINDINGS")
print("-" * 100)

for index, finding in enumerate(report.important_findings, start=1):

    print(f"{index}. {finding}")


print("\n")
print("REFERENCES")
print("-" * 100)

for index, reference in enumerate(report.references, start=1):

    print(f"{index}. {reference}")


print("\n")
print("ACTIONABLE INSIGHTS")
print("-" * 100)

for index, insight in enumerate(report.actionable_insights, start=1):

    print(f"{index}. {insight}")


print("\n")
print("LIMITATIONS")
print("-" * 100)

for index, limitation in enumerate(report.limitations, start=1):

    print(f"{index}. {limitation}")


print("\n")
print("=" * 100)
print("AUTONOMOUS RESEARCH PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 100)