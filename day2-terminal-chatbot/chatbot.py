import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_history = [
    {"role":"system", "content":"You are a helpeful assistance"}
]
print("Chatbot is running! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    chat_history.append(
        {"role":"user", "content":user_input}
    )

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = chat_history
    )

    reply = response.choices[0].message.content
    print(f"Assistant: {reply}\n")

    chat_history.append(
        {"role":"assistant","content":reply}
    )