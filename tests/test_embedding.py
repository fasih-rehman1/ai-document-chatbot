from src.embeddings import EmbeddingGenerator

embedding = EmbeddingGenerator()

model = embedding.get_embedding_model()

vector = model.embed_query("Hello World")

print(vector)