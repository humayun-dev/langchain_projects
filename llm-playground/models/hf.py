# Selecting the Hugging Face Model

from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import config.settings as settings

def get_hf_model():
    return HuggingFaceEndpoint(
        repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
        temperature = 0.7,
        huggingfacehub_api_token=settings.HUGGINGFACE_API_KEY
    )

def get_hf_model():
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=0.7,
        huggingfacehub_api_token=settings.HUGGINGFACE_API_KEY,
    )
    return ChatHuggingFace(llm=llm)