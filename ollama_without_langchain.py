import ollama

response = ollama.chat(
    model="gemma3:latest",
    messages=[
        {"role": "user", "content": "You are a helpful assistant."},
    ])

print(response['message']['content'])