import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def preprocess_text(text):
    # elimin caracterele speciale si transform textul in litere mici
    text = re.sub(r'\W+', ' ', text)
    text = text.lower()
    # eliminare spațiile suplimentare
    text = re.sub(r'\s+', ' ', text).strip()
    return text

pdf_texts = []
# extragere din fisierul urmator
for pdf in ["assets/WF-RAC-USER’S MANUAL_english.pdf"]:
    pdf_texts.append(extract_text_from_pdf(pdf))

# preprocesarea text, conform functiei de mai sus
cleaned_texts = [preprocess_text(text) for text in pdf_texts]
