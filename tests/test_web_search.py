# run : python test_web_search.py
from agent.planner import ResearchPlanner

from models.schemas import UserQuery

from search.source_selector import SourceSelector

from search.web_search import TavilySearch


planner = ResearchPlanner()

selector = SourceSelector()

search = TavilySearch()


query = UserQuery(
    query="Latest AI Regulations in Europe"
)

plan = planner.create_plan(query)

tasks = selector.create_search_tasks(plan)

results = search.search(tasks[0])

print()

for result in results:

    print("=" * 80)

    print(result.title)

    print(result.url)

    print(result.snippet[:200])

    print()