import asyncio

from agent.planner import ResearchPlanner
from extraction.content_extractor import ContentExtractor
from models.schemas import UserQuery
from processing.cleaner import DocumentCleaner
from processing.context_builder import ContextBuilder
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
builder = ContextBuilder()


query = UserQuery(
    query="Latest AI Regulations in Europe"
)

# Step 1 - Create Research Plan
plan = planner.create_plan(query)

# Step 2 - Create Search Tasks
tasks = selector.create_search_tasks(plan)

# Step 3 - Search
results = asyncio.run(
    parallel.search(tasks)
)

# Step 4 - Extract Content
documents = []

for result in results:

    document = extractor.extract(result)

    if document:
        documents.append(document)

# Step 5 - Clean
documents = cleaner.clean_documents(documents)

# Step 6 - Remove Duplicates
documents = deduplicator.remove_duplicates(documents)

# Step 7 - Filter Relevant Documents
documents = filterer.filter_documents(
    query=query.query,
    documents=documents,
    top_k=8
)

# Step 8 - Build Context
context = builder.build(documents)

print("\n")
print("=" * 100)
print("CONTEXT PREVIEW")
print("=" * 100)
print()

print(context[:5000])

print()

print("=" * 100)
print(f"Context Length : {len(context)} characters")
print(f"Documents Used : {len(documents)}")
print("=" * 100)