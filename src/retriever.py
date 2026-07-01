from langchain_chroma import Chroma

class Retriever:
    
    def __init__(self, embedding_model):
        self.db = Chroma(
            persist_directory= "vectorstore",
            embedding_function= embedding_model
            
        )
        
    def search(self, question, k=3):
        results = self.db.similarity_search_with_score(
            question,
            k=k
        )
        
        return results
    
    