# 🧠 GenAI Foundations – From Beginner to Pro

Welcome to my learning journey in Generative AI using LLMs like GPT-3.5, Mistral, and LangChain!  
This repo tracks hands-on projects as I prepare for the **Databricks Generative AI Engineer Associate** certification.

---

## 📚 Table of Contents

| Week | Topic                         | Project Folder                  |
|------|-------------------------------|----------------------------------|
| 1    | LLM Theory + Tokenization     | [`day1-llm-foundations`](./day1-llm-foundations) |
| 1    | Build Terminal Chatbot (GPT)  | [`day2-terminal-chatbot`](./day2-terminal-chatbot) |
| 1    | Prompt Engineering 101        | [`day3-prompt-engineering`](./day3-prompt-engineering) |
| 2    | LangChain & RAG               | _(coming soon)_ |
| 3–4  | Fine-Tuning & Open Models     | _(coming soon)_ |

---

## ✅ Progress Tracker

- [x] Day 1 – LLM Foundations
- [x] Day 2 – Terminal Chatbot
- [x] Day 3 – Prompt Engineering
- [ ] Day 4 – Custom AI Assistant
- [ ] Day 5 – Web UI with Streamlit
- [ ] Week 2 – Chat with your Data (LangChain + RAG)
- [ ] Week 3+ – Fine-tuning & Open Source LLMs

---

## 🛠️ Technologies Used

- 🧠 OpenAI GPT-3.5 (via API)
- 🐍 Python + Jupyter Notebooks
- 🧪 Prompt Engineering
- 📦 `openai` + `dotenv` libraries
- 💻 VS Code (with Jupyter extension)
- ⚙️ Streamlit (coming soon)
- 🧠 LangChain (coming soon)

---

## 🚀 How to Run the Projects

Clone this repo and navigate into any day’s folder:

```bash
git clone https://github.com/fmwega/genai-Foundations.git
cd genai-Foundations/day2-terminal-chatbot

# Install dependencies
pip install openai python-dotenv

# Create .env with your OpenAI API key
echo "OPENAI_API_KEY=sk-..." > .env

# Run the project
python chatbot.py
