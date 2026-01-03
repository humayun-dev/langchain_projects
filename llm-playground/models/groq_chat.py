# Method to define the Grok chat model

from langchain_groq import ChatGroq

def get_groq_model():
    return ChatGroq(
        model = "llama-3.3-70b-versatile",
        temperature=0.7
    ) 