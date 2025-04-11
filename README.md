# GenAI Foundations – From Beginner to Pro

This repository documents my learning journey in Generative AI using tools like GPT-3.5, LangChain, Streamlit, and Databricks. It includes practical, hands-on projects to build real-world skills while preparing for the Databricks Generative AI Engineer Associate certification.

---

## Table of Contents

| Week | Topic                          | Project Folder                                |
|------|--------------------------------|------------------------------------------------|
| 1    | LLM Theory + Tokenization      | [`day1-llm-foundations`](./day1-llm-foundations) |
| 1    | Build Terminal Chatbot (GPT)   | [`day2-terminal-chatbot`](./day2-terminal-chatbot) |
| 1    | Prompt Engineering 101         | [`day3-prompt-engineering`](./day3-prompt-engineering) |
| 1    | Custom AI Assistant (Profiles) | [`day4-custom-ai-assistant`](./day4-custom-ai-assistant) |
| 2    | Streamlit Web Assistant        | [`project1-web-assistant-app`](./project1-web-assistant-app) |
| 2    | LangChain & RAG                | _(coming soon)_ |
| 3–4  | Fine-Tuning & Open Models      | _(coming soon)_ |

---

## Progress Tracker

- [x] Day 1 – LLM Foundations
- [x] Day 2 – Terminal Chatbot
- [x] Day 3 – Prompt Engineering
- [x] Day 4 – Custom AI Assistant
- [x] Day 5 – Web UI with Streamlit
- [ ] Week 2 – Chat with Your Data (LangChain + RAG)
- [ ] Week 3+ – Fine-Tuning and Open Source LLMs

---

## Technologies Used

- OpenAI GPT-3.5 (API)
- Python 3.x
- Jupyter Notebooks
- Prompt Engineering
- Streamlit
- LangChain (coming soon)
- Databricks (certification prep)
- VS Code (Jupyter Extension)

---

## How to Run the Projects

Each folder is self-contained. Navigate to the folder and follow the instructions in its `README.md`. Example:

```bash
git clone https://github.com/fmwega/genai-Foundations.git
cd genai-Foundations/day2-terminal-chatbot

# Install dependencies
pip install -r requirements.txt

# Create .env with your OpenAI API key
echo "OPENAI_API_KEY=your-api-key-here" > .env

# Run the chatbot
python chatbot.py

# For Streamlit apps:
cd genai-Foundations/project1-web-assistant-app
streamlit run app.py
