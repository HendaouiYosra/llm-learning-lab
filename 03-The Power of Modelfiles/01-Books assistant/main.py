import ollama
response=ollama.generate(model="llama3.2",prompt="do you sell books?")
print(response.get("response"))