import pdfplumber
from docx import Document

def extract_text_from_pdf(file) -> str:
    with pdfplumber.open(file) as pdf:
        return '\n'.join([page.extract_text() or '' for page in pdf.pages])

def extract_text_from_docx(file) -> str:
    doc = Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])
