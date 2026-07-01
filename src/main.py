# from loader import PDFLoader
# from chunker import TextChunker
# from vector_store import VectorStore

from embeddings import EmbeddingGenerator
from retriever import Retriever



def main():

    embedding = EmbeddingGenerator()

    embedding_model = embedding.get_embedding_model()

    retriever = Retriever(
        embedding_model
    )

    while True:

        question = input("\nAsk Question : ")

        if question.lower() == "exit":
            break

        results = retriever.search(question)

        print()

        for index, (doc, score) in enumerate(results):

            print("=" * 80)

            print(f"Chunk {index+1}")

            print(f"Score : {score:.4f}")

            print("-" * 80)

            print(doc.page_content)

            print()


if __name__ == "__main__":
    main()

# def main():
    
#     print("=" * 80)
#     print("Loading PDF...")
#     print("=" * 80)

#     loader = PDFLoader(
#         "data/Employee_Handbook_Dummy.pdf"
#     )

#     text = loader.load()

#     print("PDF Loaded")

#     print()

#     chunker = TextChunker()

#     chunks = chunker.split(text)

#     print(f"Total Chunks : {len(chunks)}")

#     print()

#     embedding = EmbeddingGenerator()

#     embedding_model = embedding.get_embedding_model()

#     print("Gemini Embedding Model Ready")

#     print()

#     vector_store = VectorStore(
#         embedding_model
#     )
    
#     # Create database
#     vector_store = VectorStore(embedding_model)

#     vector_store.create_db(chunks)

#     print("Vector Database Ready")

#     print()

#     retriever = Retriever(embedding_model)

#     while True:

#         question = input("\nAsk a Question (type 'exit' to quit): ")

#         if question.lower() == "exit":
#             print("\nGoodbye!")
#             break

#         results = retriever.search(question)

#         print("\n" + "=" * 80)
#         print("Relevant Chunks")
#         print("=" * 80)

#         for index, (doc, score) in enumerate(results):

#             print("+" * 80)
#             print(f"\nChunk {index + 1}")

#             print("-" * 80)

#             print(doc.page_content)

#             print()
            

# if __name__ == "__main__":
#     main()
