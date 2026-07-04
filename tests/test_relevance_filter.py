import asyncio

from agent.planner import ResearchPlanner
from extraction.content_extractor import ContentExtractor
from models.schemas import UserQuery
from processing.cleaner import DocumentCleaner
from processing.deduplicator import DocumentDeduplicator
from processing.relevance_filter import RelevanceFilter
from search.parallel_search import ParallelSearcher
from search.source_selector import SourceSelector


planner = ResearchPlanner()
selector = SourceSelector()
parallel = ParallelSearcher()
extractor = ContentExtractor()
cleaner = DocumentCleaner()
deduplicator = DocumentDeduplicator()
filterer = RelevanceFilter()

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

documents = cleaner.clean_documents(documents)

documents = deduplicator.remove_duplicates(documents)

documents = filterer.filter_documents(
    query=query.query,
    documents=documents
)

print(f"\nRelevant Documents: {len(documents)}\n")

for doc in documents:
    print(doc.title)