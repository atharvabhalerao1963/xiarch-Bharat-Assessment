import asyncio

from agent.planner import ResearchPlanner
from models.schemas import UserQuery
from search.parallel_search import ParallelSearcher
from search.source_selector import SourceSelector


planner = ResearchPlanner()
selector = SourceSelector()
parallel = ParallelSearcher()

query = UserQuery(
    query="Latest AI Regulations in Europe"
)

plan = planner.create_plan(query)

tasks = selector.create_search_tasks(plan)

results = asyncio.run(
    parallel.search(tasks)
)

print(f"\nTotal Results: {len(results)}\n")

for result in results[:5]:

    print(result.title)