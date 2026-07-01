from langchain_chroma import Chroma
import os 
import shutil

class VectorStore:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
    
    def create_db(self , chunks):
        if os.path.exists("vectorstore"):
            shutil.rmtree("vectorstore")
            
        db = Chroma.from_texts(
            texts = chunks,
            embedding = self.embedding_model,
            persist_directory="vectorstore"
        )
        
        return db