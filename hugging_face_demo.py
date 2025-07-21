import os
from dotenv import load_dotenv  # for loading environment variables

from openai import OpenAI
load_dotenv(override=True) # override=True allows to overwrite existing variables


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Instruct",
    messages=[
        {
            "role": "user",
            "content": "capital of France",
        }
    ],
)

print(completion.choices[0].message)