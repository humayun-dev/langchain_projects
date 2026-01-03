# selecting the Gemini Model

from langchain_google_genai import ChatGoogleGenerativeAI

def get_gemini_model():
    return ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature = 0.7
    )