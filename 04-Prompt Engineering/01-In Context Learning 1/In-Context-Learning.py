import ollama

model = "deepseek-r1:1.5b"

prompt = """
Question: {Compare these two courses:
Course 1:

- Title: Introduction to Data Science
- Topics: Statistics, Data Visualization, Python Programming
- Prerequisites: None
- Assessment: Midterm Exam, Final Project

Course 2:

- Title: Introduction to Machine Learning
- Topics: Statistics, Python Programming, Supervised Learning, Unsupervised Learning
- Prerequisites: Intro to Programming
- Assessment: Homework Assignments, Final Project
}
Answer :{

# **Similarities:**

- Topics: Statistics, Python Programming
- Assessment: Final Project

# **Differences:**

**Course 1:**

- Title: Introduction to Data Science
- Topics: Data Visualization
- Prerequisites: None
- Assessment: Midterm Exam

**Course 2:**

- Title: Introduction to Machine Learning
- Topics: Supervised Learning, Unsupervised Learning
- Prerequisites: Intro to Programming
- Assessment: Homework Assignments

# **Conclusion:**

These two courses share some foundational content, particularly in statistics and Python programming, but they focus on different goals. Course 1 emphasizes general data science skills and visualization, while Course 2 focuses on core machine learning techniques and includes more continuous assessment.
}
Question:{ Compare these two courses:

Course 1:

- Title: Ancient Civilizations
- Topics: Mesopotamia, Ancient Egypt, Ancient Greece, Ancient China
- Prerequisites: None
- Assessment: Research Paper, Final Exam

Course 2:

- Title: Introduction to World Literature
- Topics: Greek Mythology, Shakespeare, Postcolonial Literature
- Prerequisites: None
- Assessment: Essays, Final Exam
}

Answer:{

# **Similarities:**

- Prerequisites: None
- Assessment: Final Exam

# **Differences:**

**Course 1:**

- Title: Ancient Civilizations
- Topics: Mesopotamia, Ancient Egypt, Ancient China
- Assessment: Research Paper

**Course 2:**

- Title: Introduction to World Literature
- Topics: Greek Mythology, Shakespeare, Postcolonial Literature
- Assessment: Essays

# **Conclusion:**

These two courses share a general focus on humanities and historical content, but they cover entirely different subject areas — ancient history versus literary analysis. Their assessment styles also differ, with Course 1 emphasizing research papers and Course 2 focusing on essays.
} 
Question:{ Compare these two courses 
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
- Assessment: Midterm, Final, Assignments} 
Answer :
"""

response = ollama.generate(model=model, prompt=prompt)

# Define output path
output_path = "./output/report.md"

# Save the response directly as Markdown file
with open(output_path, "w", encoding="utf-8") as md_file:
    md_file.write("# Course Equivalency Report\n\n")
    md_file.write(response["response"])

print(f"Saved equivalency report to {output_path}")
