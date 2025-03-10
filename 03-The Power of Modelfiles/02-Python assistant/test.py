import ollama
model="python-model"
response=ollama.generate(model=model, prompt="give a function that adds numbers from 1 to n given n as a parameter")
print(response.get("response",""))