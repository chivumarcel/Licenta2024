import openai #update 14.07.2024, 14:20+, v04
import os
from dotenv import load_dotenv #in order to use the api key from .env
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import fitz  # PyMuPDF - for extracting texts from PDF files

# load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # set API key via .env file

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# extracting text from PDFs and concatenate
pdf_files = ["assets/WF-RAC-Connection_manual_with_Alexa.pdf",
             "assets/WF-RAC-Connection_manual_with_Google.pdf",
             "assets/WF-RAC-Setup_Quick_Guide_to_the_Remote_Control_System_Configuration_for_RAC.pdf",
             "assets/WF-RAC-Databook.pdf",
             "assets/WF-RAC-Smart_M-Air_AppManual-English(EEA,UK).pdf",
             "assets/WF-RAC-Smart_m_air_FAQ_english.pdf",
             "assets/WF-RAC-USER’S MANUAL_english.pdf",
             "assets/WF-RAC-Wireless LAN connection manual_EN_Web ZTL.pdf",
             "assets/WF_RAC-INSTALLATION MANUAL_english.pdf",
             "assets/WF_RAC-Wireless LAN connection manual_EN_Web ZSX.pdf"
             ]
pdf_text = "\n".join([extract_text_from_pdf(pdf) for pdf in pdf_files])

# saving the extracted text to a file
with open("extracted_text.txt", "w") as text_file:
    text_file.write(pdf_text)

# links to be included for more precise answers
links = [
    {"title": "Aparate de aer conditionat Mitsubishi Electric MSZ-HR35VF 12000 BTU, Clasa A++, filtru anti-praf, functie Econo Cool, alb",
     "url": "https://licenta.aiwizz.ro/product/aparate-de-aer-conditionat-mitsubishi-electric-msz-hr35vf-12000-btu-clasa-a-filtru-anti-praf-functie-econo-cool-alb/"},
    {"title": "Unitate interna pentru aer conditionat, Mitsubishi HR, 14000 BTU, MSZ-HR42,Clasa A++/A++",
     "url": "https://licenta.aiwizz.ro/product/unitate-interna-pentru-aer-conditionat-mitsubishi-hr-14000-btu-msz-hr42clasa-a-a-2/"},
]

#links_text = "\n".join([f"{link['title']}: {link['url']}" for link in links])
links_html = "\n".join([f'<a href="{link["url"]}">{link["title"]}</a>' for link in links])

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

chat_log = [{"role":"system",
             "content":"Your name is Nea Gicu. You are a technical chatbot and a sales representative that helps users that arrive on our website to make better decisions \
             about buying air conditioning equipment. Please help users with clear instructions on how to use and buy our products from OUR website - aiwizz.ro. \
             Do not send or reccommend users to buy products from other websites. Please respond in Romanian language. If you do not know how to answer a question, say: Nu va pot raspunde la aceasta intrebare, \
             dar va pot recomanda unui coleg uman din cadrul departamentului Suport si acesta va va raspunde solicitarii dvs. Multumesc! \
            Here is some additional information from our documents: {pdf_text}. \nHere are some useful links for specific questions about products and prices: {links_html}"

            }]

chat_responses = []

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    chat_log.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        temperature=0.5
    )

    bot_response = response["choices"][0]["message"]["content"]
    chat_log.append({"role": "assistant", "content": bot_response})

    # adaugare raspunsuri in chat_responses pentru a fi afișate
    chat_responses.append(f"Vizitator: {user_input}")
    chat_responses.append(f"ChatBot: {bot_response}")

    # inversez ordinea mesajelor pentru afișare
    chat_contents = chat_responses[::-1]

    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_contents})



