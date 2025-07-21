
from dotenv import load_dotenv  # for loading environment variables
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv(override=True) # override=True allows to overwrite existing variables

# Initialize the Google Generative AI chat model
llm= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the model to use
    temperature=0.7,  # Set the temperature for response variability
    max_tokens=1000,  # Set the maximum number of tokens in the response
)

# Example usage of the Google Generative AI model
response = llm.invoke("What is the capital of France?")
# Print the response
print(response.content)