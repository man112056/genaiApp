from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    ("system", "You are a helpful assistant."),
    ("human", "Asnwer the following question: {question}"),
)
llm = ChatOllama(
    model="gemma3",)

chain = prompt | llm  # example of chaining prompt will be input to llm
response = chain.invoke({"question": "write a code to print hello world in python"})
print(response)  # prints the response from the LLM