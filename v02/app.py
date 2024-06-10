from flask import Flask, request, jsonify
import openai
import fitz  # PyMuPDF
import re

app = Flask(__name__)
openai.api_key = '##'

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def preprocess_text(text):
    text = re.sub(r'\W+', ' ', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

pdf_texts = []
for pdf in ["assets/WF-RAC-USER’S MANUAL_english.pdf"]:
    pdf_texts.append(extract_text_from_pdf(pdf))

cleaned_texts = [preprocess_text(text) for text in pdf_texts]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    context = " ".join(cleaned_texts)
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=f"{context}\n\nUser: {user_input}\nBot:",
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(port=5000)
