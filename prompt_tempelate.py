
from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["question"],
    template="Asnwer the following question: {question}",
)

llm = ChatOllama(
    model="gemma3",)

chain = prompt | llm  #  example of chaining promt will be input to llm 
# above code is example of sequential chaining of prompt and llm. 
# there is something called parallel chaining as well. 
#LCEL = LangChain Expression Language
# it is a way to express the chaining of components in LangChain.
response = chain.invoke({"question": "write a code to print hello world in python"})
 # invoke method is used to call the chain with input where input is a dictionary with key as input variable name and value as input value
print(response)  # prints the response from the LLM

# Note: ChatpomptTempelte is used in other files like hugging_face_demo.py, groq_demo.py, google_gemini.py