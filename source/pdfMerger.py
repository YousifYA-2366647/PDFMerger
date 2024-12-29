import pypdf

"""
    Function takes a list of pdf files, merges them and writes the result to the given output file.

    Parameters: 
        - pdfFiles: a list of pdf-file paths
        - output: path to the output file

    Exceptions:
        - If a pdf-file is not found on the current device, this function will throw an error and skip the file that was not found.

    Pre-conditions:
        - The elements in the given list must be paths to existing files.

    Post-conditions:
        - The path that output represents will contain the results.
"""
def mergePdf(pdfFiles: list[str], output: str) -> None:
    merger = pypdf.PdfWriter()

    for file in pdfFiles:
        try:
            with open(file, "rb") as openedFile:
                merger.append(fileobj=openedFile)
        except FileNotFoundError as err:
            print("File not found. \n")
            print(err)
            
    try:
        with open(output, "wb") as outputFile:
            merger.write(outputFile)
    except FileNotFoundError as err:
            print("File not found. \n")
            print(err)
    merger.close()