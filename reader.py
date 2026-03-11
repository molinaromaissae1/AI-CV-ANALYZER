import pdfplumber
import docx

def read_cv(file):

    text = ""

    if file.name.endswith(".pdf"):

        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text

    elif file.name.endswith(".docx"):

        doc = docx.Document(file)

        for p in doc.paragraphs:
            text += p.text

    return text
