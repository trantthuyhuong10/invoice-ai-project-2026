import pdfplumber
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except:
        pass

    if not text.strip():
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img)

    return text