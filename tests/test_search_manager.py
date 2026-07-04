# run : test_serach_manager.py 
from agent.planner import ResearchPlanner
from models.schemas import UserQuery
from search.source_selector import SourceSelector
from search.search_manager import SearchManager


planner = ResearchPlanner()

selector = SourceSelector()

manager = SearchManager()


query = UserQuery(
    query="Latest AI Regulations in Europe"
)

plan = planner.create_plan(query)

tasks = selector.create_search_tasks(plan)

execution_plan = manager.prepare_execution(tasks)

print()

for task in execution_plan:
    print(task)