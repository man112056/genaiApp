from langchain_ollama.chat_models import ChatOllama


llm = ChatOllama(model="gemma3:latest")
response = llm.invoke("tell me about agentic api")
print(response.content)