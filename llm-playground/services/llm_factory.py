# Dynamic model selector

from models.groq_chat import get_groq_model
from models.gemini_chat import get_gemini_model
from models.hf import get_hf_model

def get_llm(provider: str):
    if provider == "groq":
        return get_groq_model()
    elif provider == "gemini":
        return get_gemini_model()
    elif provider == "huggingface":
        return get_hf_model()
    else:
        raise ValueError("Unsupported LLM provider") 
