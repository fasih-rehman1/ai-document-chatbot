from dotenv import load_dotenv
import os

#load .env file
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME  = os.getenv("MODEL_NAME")
    APP_NAME = os.getenv("APP_NAME")
    DEBUG = os.getenv("DEBUG")