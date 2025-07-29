from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


model = ChatOllama(
    model = "gemma3"
)

prompt = PromptTemplate(
    template="Extract the title from the following webpage: {url}",
    input_variables=["question", "text"]
)   

loader = WebBaseLoader(
    url="https://www.example.com",
    model=model,
    prompt=prompt,
    output_parser=StrOutputParser()

document = loader.load()
chain = model | prompt | parser
response = chain.invoke({"url": "https://www.example.com"})
# print(response)