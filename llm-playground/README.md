# Multi-LLM Playground – Beginner-Friendly LLM Project

 **Why This Project?**

If you’re starting with **Generative AI / LLMs**, jumping directly into complex systems like RAG or agents can feel overwhelming.  
This project is designed as:  

✅ A first LLM project  
✅ Focused on core fundamentals  
✅ Easy to extend into advanced use cases  

---

##  What This App Does

- Accepts a user prompt  
- Runs the same prompt across **multiple LLMs**  
- Displays:  
  - Model responses  
  - Response time (latency)  
- Helps users:  
  - Compare output quality  
  - Understand performance differences  
  - Learn how LLM APIs are used in practice  

---

##  Concepts Covered (Beginner Level)

- LLM abstraction  
- Prompt → response flow  
- Working with multiple providers  
- Measuring response latency  
- Error handling in LLM APIs  
- Building simple AI UIs  

---

##  Tech Stack

- Python  
- Streamlit – UI  
- LangChain – LLM abstraction  
- Google Gemini  
- Groq  
- Hugging Face Models  
- Pandas – latency comparison table  

---

##  Application Flow

1. User enters a prompt  
2. User selects one or more LLM providers  
3. App sends the prompt to each model  
4. Responses and latency are collected  
5. Results are displayed side-by-side  

---

##  Example Features

- Multi-model comparison  
- Latency measurement (response time)  
- Expandable response sections  
- Clean and simple UI  
- Beginner-readable code structure  

---

##  Setup Instructions

###  Clone the Repository
```bash
git clone https://github.com/humayun-dev/multi-llm-playground.git
cd multi-llm-playground
