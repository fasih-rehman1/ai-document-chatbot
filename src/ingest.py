from loader import PDFLoader
from chunker import TextChunker
from embeddings import EmbeddingGenerator
from vector_store import VectorStore


print("=" * 80)
print("Reading PDF...")
print("=" * 80)

loader = PDFLoader(
    "data/Employee_Handbook_Dummy.pdf"
)

text = loader.load()

chunker = TextChunker()

chunks = chunker.split(text)

embedding = EmbeddingGenerator()

embedding_model = embedding.get_embedding_model()

db = VectorStore(
    embedding_model
)

db.create_db(chunks)

print()

print("Vector Database Created Successfully")