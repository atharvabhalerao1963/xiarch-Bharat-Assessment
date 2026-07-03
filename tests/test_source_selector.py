from agent.planner import ResearchPlanner
from models.schemas import UserQuery
from search.source_selector import SourceSelector


planner = ResearchPlanner()

selector = SourceSelector()

query = UserQuery(
    query="Latest AI Regulations in Europe"
)

plan = planner.create_plan(query)

tasks = selector.create_search_tasks(plan)

print()

for task in tasks:
    print(task)