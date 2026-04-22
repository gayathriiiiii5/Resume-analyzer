import PyPDF2
def extract_text(file):
    text=file.read()
    reader=PyPDF2.PdReader(file)
    for page in reader.pages:
        text+=page.extract_text()
        return text