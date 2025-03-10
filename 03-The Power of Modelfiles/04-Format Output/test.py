import ollama

model = "equivalency-modelqwen:latest"

prompt = """
Compare these two course outlines and determine if they are equivalent for credit transfer. Provide a structured justification.

Course 1:
- Title: Data Structures & Algorithms
- Topics: Arrays, Linked Lists, Trees, Graphs, Sorting, Hashing
- Credits: 3
- Prerequisites: Intro to Programming
- Assessment: Midterm, Final, Project

Course 2:
- Title: Advanced Data Structures
- Topics: Trees, Graphs, Hashing, Dynamic Programming
- Credits: 4
- Prerequisites: Object-Oriented Programming
- Assessment: Midterm, Final, Assignments
"""

response = ollama.generate(model=model, prompt=prompt)

# Define output path
output_path = "./data/report.md"

# Save the response directly as Markdown file
with open(output_path, "w", encoding="utf-8") as md_file:
    md_file.write("# Course Equivalency Report\n\n")
    md_file.write(response["response"])

print(f"Saved equivalency report to {output_path}")
