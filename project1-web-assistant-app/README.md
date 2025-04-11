# Streamlit AI Assistant – Web Chat App

This is a customizable AI assistant built with OpenAI's GPT-3.5 and Streamlit. It allows users to choose different assistant personalities and have real-time conversations through a simple web interface.

## Features

- Chat with GPT-3.5 via the OpenAI API
- Choose from multiple assistant profiles:
  - Default, Formal, Casual, Study Coach, ChefAI, Pirate, JSON Bot
- Saves chat memory to disk
- Remembers session history using Streamlit's session state
- "Clear Chat" button to reset conversation
- Deployable on Streamlit Cloud

## Requirements

- Python 3.8 or higher
- OpenAI API key

## Installation (Local)

1. Clone the repository

```bash
git clone https://github.com/your-username/project1-web-assistant-app.git
cd project1-web-assistant-app

## Run the app
streamlit run app.py
