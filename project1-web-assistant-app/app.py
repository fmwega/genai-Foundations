import os
import json
import openai
import streamlit as st
from dotenv import load_dotenv, find_dotenv

#load .env file
load_dotenv(find_dotenv(), override=True)
openai.api_key = os.getenv("OPENAI_API_KEY")

# personality profiles
assistant_profiles = {
    "Default": "You are a helpful assistant.",
    "Formal": "You are a professional assistant. Use formal tone and avoid emojis.",
    "Casual": "You are a casual, friendly assistant. Use light humor and emojis.",
    "Study_coach": "You are a motivational study coach. Encourage the user and break topics into steps.",
    "ChefAI":"You are ChefAI 👨‍🍳, a friendly and helpful cooking assistant who gives recipes with emojis and step-by-step instructions.",
    "Pirate": "You are a pirate. Speak only in pirate language.",
    "Json_bot": "You are a bot that always responds in structured JSON format."
}
#create a memory file
MEMORY_FILE = "memory.json"

#load memory file
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []
#save_memory file
def save_memory(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

#set streamlit page config
st.set_page_config(page_title="AI Assistant", layout="centered")
st.title("Custom AI Assistant")

#sidebar for role selection
profile = st.sidebar.selectbox("Choose an assistance profile", list(assistant_profiles.keys()))

#session state for chat history
if "chat_history" not in st.session_state or st.session_state.get("last_profile") != profile:
    st.session_state.chat_history = [{"role":"system", "content":assistant_profiles[profile]}]
    st.session_state.last_profile = profile

#user input box
user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.chat_history.append({"role":"user","content":user_input})

    try:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=st.session_state.chat_history[-10:] #limit context to 10
        )

        reply = response["choices"][0]["message"]["content"]
        st.session_state.chat_history.append({"role":"assistant","content":reply})
        save_memory(st.session_state.chat_history)

    except Exception as e:
        reply = f"Error: {e}"
        st.session_state.chat_history.append({"role":"assistant","content":reply})

#display full chat
for msg in st.session_state.chat_history:
    if msg ["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg ["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
        