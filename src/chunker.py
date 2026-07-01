from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextChunker:
    """
    Splits large text into smaller chunks.
    """
    def __init__(self, chunk_size=200, chunk_overlap=40):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size= chunk_size,
            chunk_overlap = chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )
    
    def split(self, text):
        return self.splitter.split_text(text)