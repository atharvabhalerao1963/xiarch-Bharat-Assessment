import asyncio

from agent.planner import ResearchPlanner
from extraction.content_extractor import ContentExtractor
from models.schemas import UserQuery
from processing.cleaner import DocumentCleaner
from search.parallel_search import ParallelSearcher
from search.source_selector import SourceSelector


planner = ResearchPlanner()
selector = SourceSelector()
parallel = ParallelSearcher()
extractor = ContentExtractor()
cleaner = DocumentCleaner()

query = UserQuery(
    query="Latest AI Regulations in Europe"
)

plan = planner.create_plan(query)

tasks = selector.create_search_tasks(plan)

results = asyncio.run(
    parallel.search(tasks)
)

documents = []

for result in results:

    document = extractor.extract(result)

    if document:
        documents.append(document)

clean_documents = cleaner.clean_documents(documents)

print()

print(f"Documents: {len(clean_documents)}")

print()

print(clean_documents[0].content[:1000])