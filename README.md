# 🧠 GenAI Foundations – From Beginner to Pro

Welcome to my learning journey in Generative AI using LLMs like GPT-3.5, Mistral, and LangChain! This repo tracks hands-on projects as I study toward the **Databricks Generative AI Engineer Associate** certification.

---

## 📚 Table of Contents

| Week | Topic                         | Project Folder                  |
|------|-------------------------------|----------------------------------|
| 1    | LLM Theory + Tokenization     | [`day1-llm-foundations`](./day1-llm-foundations) |
| 1    | Build Terminal Chatbot (GPT)  | [`day2-terminal-chatbot`](./day2-terminal-chatbot) |
| 2    | LangChain & RAG               | _(coming soon)_ |
| 3–4  | Fine-Tuning & Open Models     | _(coming soon)_ |

---

## 🛠️ Technologies Used
- OpenAI GPT-3.5
- Python & Jupyter
- VS Code
- Streamlit (soon)
- LangChain (soon)

---

## 🚀 How to Run the Projects

Clone this repo and navigate to any project:

```bash
git clone https://github.com/fmwega/genai-Foundations.git
cd genai-Foundations/day2-terminal-chatbot

# Install dependencies
pip install openai python-dotenv

# Add your OpenAI key
echo "OPENAI_API_KEY=sk-..." > .env

# Run it
python chatbot.py
