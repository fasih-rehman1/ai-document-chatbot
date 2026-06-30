from loader import PDFLoader


def main():
    pdf = PDFLoader("data/Employee_Handbook_Dummy.pdf")

    text = pdf.load()

    print("=" * 80)
    print(text)
    print("=" * 80)


if __name__ == "__main__":
    main()