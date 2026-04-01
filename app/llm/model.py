import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_llm():
    mistral_api_key = os.getenv("MISTRAL_API_KEY")
    if not mistral_api_key:
        raise ValueError("MISTRAL_API_KEY is not set in the environment variables.")
    
    return ChatMistralAI(model="mistral-large-latest") 


def get_google_llm():
    google_api_key = os.getenv("GEMINI_API_KEY")
    if not google_api_key:
        raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)