# LLM initialization

from langchain_groq import ChatGroq
from config.settings import MODEL_NAME,TEMPERATURE

def get_llm():
    return ChatGroq(
        model = MODEL_NAME,
        temperature = TEMPERATURE
    )