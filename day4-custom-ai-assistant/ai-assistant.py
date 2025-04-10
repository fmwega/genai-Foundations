'''
I created a custom AI assistant chatbot that:
Talks to you in the terminal
Lets you choose its personality (e.g. professional, funny, pirate)
Remembers what you say in a session
Talks back using OpenAI's GPT model
'''
# Import tools and Load API Key
import os
import openai
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define Assistant Profiles
assistant_profiles = {
    "professional": "You are a professional assistant. Use formal tone and avoid emojis.",
    "casual": "You are a casual, friendly assistant. Use light humor and emojis.",
    "study_coach": "You are a motivational study coach. Encourage the user and break topics into steps.",
    "pirate": "You are a pirate. Speak only in pirate language.",
    "json_bot": "You are a bot that always responds in structured JSON format."
}

#Load Memory from File
#This is the file where we’ll save conversation history so the assistant remembers things

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history,f, indent=2)

#Run the Assistant (Main Program)
#Shows the list of personalities (professional, casual, etc.)

def run_assistant():
    print("Choose on assistant profile: ")
    for key in assistant_profiles:
        print(f"-{key}")
    
    #If you type something invalid, it uses the casual personality by default.
    selected = input("Profile name: ").strip().lower()
    system_prompt = assistant_profiles.get(selected, assistant_profiles["casual"])

    chat_history = [{"role":"system", "content":system_prompt}]
    chat_history += load_memory()

    #Lets you type messages to the assistant
    #Ends the chat if you type exit or quit
    print("Your assistant is online! (type 'exit' to quit) \n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
            
        chat_history.append({"role":"user", "content": user_input})

        #Sends the system message + last 10 messages to OpenAI
        try:
            context = chat_history[-10:] if len(chat_history) > 10 else chat_history

            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = context
            )

            #Get the assistant’s reply
            reply = response["choices"][0]["message"]['content']
            print(f"Assistant: {reply}\n")

            #Save assistant reply to history and adds to memory
            chat_history.append({"role":"assistant", "content":reply})
            save_memory(chat_history)

        #if something fails (like bad internet or wrong API key), it shows an error message
        except Exception as e:
            print("Error: ", e)

if __name__=="__main__":
    run_assistant()
    