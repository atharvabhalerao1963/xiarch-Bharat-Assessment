# python test_content_extractor.py
from agent.planner import ResearchPlanner

from extraction.content_extractor import ContentExtractor

from models.schemas import UserQuery

from search.parallel_search import ParallelSearcher

from search.source_selector import SourceSelector

import asyncio


planner = ResearchPlanner()

selector = SourceSelector()

parallel = ParallelSearcher()

extractor = ContentExtractor()


query = UserQuery(
    query="Latest AI Regulations in Europe"
)

plan = planner.create_plan(query)

tasks = selector.create_search_tasks(plan)

results = asyncio.run(
    parallel.search(tasks)
)

document = extractor.extract(
    results[0]
)

print()

print(document.title)

print()

print(document.content[:1000])