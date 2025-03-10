import ollama

model = "llama3.2"
output_file = "output-numctx.txt"  # File to store responses

# Conversation prompts
prompts = [
    "Hello, my name is Yosra.",
    """Benny was a little bunny who loved to explore the forest. Every morning, he hopped around, looking for new adventures. He enjoyed the fresh air, the rustling leaves, and the soft earth beneath his paws.

    One day, Benny found a shiny red apple under a big oak tree. He was so happy! But just as he was about to take a bite, a gust of wind rolled the apple down a hill.

    "Oh no!" Benny cried and ran after it.
    little one. And remember, sometimes a little adventure makes things even sweeter.""",
    "What's my name?",
    """Benny was a little bunny who loved to explore the forest. Every morning, he hopped around, looking for new adventures. He enjoyed the fresh air, the rustling leaves, and the soft earth beneath his paws.

    One day, Benny found a shiny red apple under a big oak tree. He was so happy! But just as he was about to take a bite, a gust of wind rolled the apple down a hill.

    "Oh no!" Benny cried and ran after it.

    The apple rolled faster and faster. Benny hopped as quickly as he could, but the apple was too fast. It rolled into a small cave at the bottom of the hill.

    Benny stopped outside the cave. It was dark inside, and he felt a little scared. But he really wanted his apple. So, he took a deep breath and stepped inside.

    Inside the cave, Benny saw glowing fireflies lighting up the walls. Their tiny lights flickered like stars, making the cave look magical. In the middle of the cave sat a friendly old turtle, wearing a small pair of glasses.

    "Hello, little bunny," said the turtle with a warm smile. "Are you looking for something?"

    "Yes!" Benny said. "My apple rolled in here."

    The turtle chuckled. "Ah, I see! It stopped right by my shell."

    He nudged the apple toward Benny. The bunny’s eyes lit up with joy.

    "Thank you so much!" Benny said. """,
    "What's my name?"
]

def chat_with_model(num_ctx_value):
    """Run a conversation with the model using a given num_ctx and return the responses."""
    conversation_history = []
    responses = []

    for user_input in prompts:
        conversation_history.append({"role": "user", "content": user_input})
        response = ollama.chat(
            model=model,
            messages=conversation_history,
            options={"num_ctx": num_ctx_value, "num_predict": 20}
        )
        model_response = response['message']['content'].strip()
        conversation_history.append({"role": "assistant", "content": model_response})
        # Store response
        responses.append(f"User: {user_input}\nModel: {model_response}\n")

    return responses


# Run the test for both num_ctx values and store results
with open(output_file, "w", encoding="utf-8") as file:
    file.write("===== TEST WITH num_ctx = 256 (Forgetful) =====\n")
    responses_256 = chat_with_model(256)
    file.writelines(responses_256)

    file.write("\n\n===== TEST WITH num_ctx = 1024 (Better Memory) =====\n")
    responses_1024 = chat_with_model(1024)
    file.writelines(responses_1024)

print(f"Results saved in {output_file}")
