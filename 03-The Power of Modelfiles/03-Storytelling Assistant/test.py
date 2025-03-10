import ollama

model = "story-telling"
output="./output/output.txt"
response = ollama.generate(model=model, prompt="tell me a short story")

# Iterate over the streamed response to display output in real-time
print(response.get("response",""))
with open(output,"w",encoding="utf-8") as f:
    f.writelines(response.get("response",""))

