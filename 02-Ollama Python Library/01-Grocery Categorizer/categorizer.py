import ollama
import os

model="llama3.2"

input="./data/grocery.txt"
outtput="./data/categorized_grocery.txt"

if not os.path.exists(input):
    print(f"Input file '{input}' not existing")
    exit(1)

with open(input,"r") as f:
    items=f.read().strip()
print(items)

prom= f"""
You are an assitant who can categorize and sort grocery items
here is the list of grocery items:
{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""
response= ollama.generate(model=model,prompt=prom)
generated_text=response.get("response","")
print(generated_text)

with open(outtput, "w") as f:
    f.write(generated_text.strip())