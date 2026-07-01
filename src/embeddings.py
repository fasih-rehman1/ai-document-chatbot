from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import Config


class EmbeddingGenerator:

    def __init__(self):

        self.embedding = GoogleGenerativeAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            google_api_key=Config.GEMINI_API_KEY
        )

    def get_embedding_model(self):
        return self.embedding