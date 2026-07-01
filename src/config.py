from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    CHAT_MODEL = os.getenv("CHAT_MODEL")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# from dotenv import load_dotenv
# import os

# #load .env file
# load_dotenv()

# class Config:
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#     MODEL_NAME  = os.getenv("MODEL_NAME")
#     APP_NAME = os.getenv("APP_NAME")
#     DEBUG = os.getenv("DEBUG")
    
