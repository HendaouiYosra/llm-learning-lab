import ollama

response=ollama.chat(
    model="llama3.2",
    messages=[
        {"role":"user",
         "content":"why is the sky blue"
         },],
    stream=True
)
for chunk in response:
    print(chunk["message"]["content"],end="",flush=True)