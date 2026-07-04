# run : git python test_gemini.py 
from llm.client import GeminiClient

client = GeminiClient()

response = client.generate(
    "Say hello in one sentence."
)

print(response)