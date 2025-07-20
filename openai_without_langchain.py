from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI()
response = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "You are a helpful assistant."}],
)
print(response['choices'][0]['message']['content'])