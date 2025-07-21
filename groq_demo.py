import os
from groq import Groq
from dotenv import load_dotenv  # for loading environment variables
load_dotenv(override=True)  # override=True allows to overwrite existing variables  
# Initialize the Groq client
#https://console.groq.com/docs/quickstart
client = Groq(
    api_key=os.environ["GROQ_API_KEY"],
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)