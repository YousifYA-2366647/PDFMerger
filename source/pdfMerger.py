import pypdf, sys

def mergePdf(pdfFiles: list[str], output: str):
    try:
        merger = pypdf.PdfWriter()
        for file in pdfFiles:
            with open(file, "rb") as openedFile:
                merger.append(fileobj=openedFile)
        with open(output, "wb") as outputFile:
            merger.write(outputFile)
    except FileNotFoundError as err:
        print("File not found. \n")
        print(err)
        sys.exit(3)
    finally:
        merger.close()