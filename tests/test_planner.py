# run : test_planner.py
from agent.planner import ResearchPlanner

from models.schemas import UserQuery


planner = ResearchPlanner()

query = UserQuery(
    query="Latest AI Regulations in Europe"
)

plan = planner.create_plan(query)

print()

print(plan)

print()

print(plan.preferred_sources)