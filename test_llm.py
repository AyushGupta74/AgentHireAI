from services.llm_service import LLMService

llm = LLMService()

response = llm.generate(
    "Explain machine learning in one sentence."
)

print(response)
