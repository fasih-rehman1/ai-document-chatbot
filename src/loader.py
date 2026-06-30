from pathlib import Path
from pypdf import PdfReader


class PDFLoader:
    """
    A simple PDF loader that reads all pages
    and returns the extracted text.
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load(self):

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"{self.file_path} not found."
            )

        reader = PdfReader(self.file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text