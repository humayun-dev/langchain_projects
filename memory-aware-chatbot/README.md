# Memory-Aware AI Chatbot

A **Memory-Aware AI Chatbot** built with **LangChain**, **Groq LLM**, and **Streamlit**, capable of **remembering previous conversations**, providing **context-aware responses**, and demonstrating **modern conversational AI techniques**.

---

## Why This Project?

Most chatbots **forget previous messages**, leading to a poor user experience.  
This project demonstrates:

- **Persistent conversation memory**  
- **Contextual responses**  
- **Prompt engineering with dynamic templates**  
- **LangChain architecture with `RunnableWithMessageHistory`**  

## Features

- Memory-aware conversations using **LangChain session-based memory**  
- Streamlit **web UI** for interactive chatting  
- Groq **LLM integration** (supports latest Groq models)  
- Dynamic **prompt templates** for friendly, personalized responses  
- Session-based memory to remember user info across multiple messages  

## Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Groq (llama-3.1-8b-instant recommended) |
| Conversational Memory | LangChain `RunnableWithMessageHistory` |
| Prompt Engineering | LangChain `ChatPromptTemplate` |
| Web UI | Streamlit |
| Environment | Python 3.10+, virtualenv |
| Config & Secrets | `.env` file with `GROQ_API_KEY` |

---

## Project Structure

memory-aware-chatbot/
│
├── chatbot/
│ ├── llm.py # Groq LLM initialization
│ ├── prompt.py # Prompt templates
│ └── chains.py # Chain + memory integration
│
├── config/
│ └── settings.py # API key + model config
│
├── streamlit_app.py # Streamlit UI entry point for the bot
├── .env.example # Environment variable template
└── README.md 



