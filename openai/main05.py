import openai #update 14.07.2024, 13:00+, v03
import os
from dotenv import load_dotenv #in order to use the api key from .env
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import fitz  # PyMuPDF - for extracting texts from PDF files
from datetime import datetime
from markupsafe import Markup

# load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # set API key via .env file

app = FastAPI()
templates = Jinja2Templates(directory="templates")

chat_responses = []

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
    {"title": "Unitate interna pentru aer conditionat, Mitsubishi HR, 14000 BTU, MSZ-HR42,Clasa A++/A++",
     "url": "https://licenta.aiwizz.ro/product/unitate-interna-pentru-aer-conditionat-mitsubishi-hr-14000-btu-msz-hr42clasa-a-a-2/"},
    {"title": "Aparate de aer conditionat Mitsubishi Electric MSZ-HR35VF 12000 BTU, Clasa A++, filtru anti-praf, functie Econo Cool, alb",
     "url": "https://licenta.aiwizz.ro/product/aparate-de-aer-conditionat-mitsubishi-electric-msz-hr35vf-12000-btu-clasa-a-filtru-anti-praf-functie-econo-cool-alb-2/"},
    {"title": "Aer conditionat Mitsubishi Electric MSZ-HR35VF / MUZ-HR35VF R32, Wi-Fi inclus, Kit de instalare inclus, Inverter, 12000 BTU/h, Clasa A++, Filtru anti-praf, Functie Econo Cool, Timer Saptamanal, Auto-restart",
     "url": "https://licenta.aiwizz.ro/product/aer-conditionat-mitsubishi-electric-msz-hr35vf-muz-hr35vf-r32-wi-fi-inclus-kit-de-instalare-inclus-inverter-12000-btu-h-clasa-a-filtru-anti-praf-functie-econo-cool-timer-saptamanal-auto-r/"},
    {"title": "Aparat de aer conditionat Mitsubishi 18000 BTU Wi-Fi, Clasa A++/A++, Filtru special Plasma Quad Plus, Super Energy Efficient Heating, Night Mode,MSZ-AY50, alb",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-mitsubishi-18000-btu-wi-fi-clasa-a-a-filtru-special-plasma-quad-plus-super-energy-efficient-heating-night-modemsz-ay50-alb/"},
    {"title": "Aparat de aer conditionat Mitsubishi 9000 BTU Wi-Fi, Clasa A+++, Quiet Comfort, High Energy-Savings, V Blocking Filter, Stylish Line-up, Kirigamine Zen MSZ-EF25VGKB, negru",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-mitsubishi-9000-btu-wi-fi-clasa-a-quiet-comfort-high-energy-savings-v-blocking-filter-stylish-line-up-kirigamine-zen-msz-ef25vgkb-negru/"},
    {"title": "Aparat de aer conditionat Mitsubishi 12000 BTU Wi-Fi, Clasa A+++/A++, Filtru special Plasma Quad Plus, Super Energy Efficient Heating, Night Mode,MSZ-AY35, alb",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-mitsubishi-12000-btu-wi-fi-clasa-a-a-filtru-special-plasma-quad-plus-super-energy-efficient-heating-night-modemsz-ay35-alb/"},
    {"title": "Aparat de aer conditionat Mitsubishi 18000 BTU, Clasa A++, Filtru de Purificare Aer, Energy Saving, MSZ-DW50,alb",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-mitsubishi-18000-btu-clasa-a-filtru-de-purificare-aer-energy-saving-msz-dw50alb/"},
    {"title": "Aparat de aer conditionat inverter, Mitsubishi, Electric MSZ-EF50VGKW/MUZ-EF50VG Kirigamine Zen, 18.000 BTU, Clasa A++/A+, 30 dB, Freon R32, Alb",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-inverter-mitsubishi-electric-msz-ef50vgkw-muz-ef50vg-kirigamine-zen-18-000-btu-clasa-a-a-30-db-freon-r32-alb/"},
    {"title": "Aparat de aer conditionat hiperinverter, Mitsubishi, 18.000 BTU, Clasa A++/A++, 25 dB, Alb",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-hiperinverter-mitsubishi-18-000-btu-clasa-a-a-25-db-alb/"},
    {"title": "Unitate interna pentru aer conditionat, Mitsubishi LN, 9000 BTU, Clasa A+++/A+++, Solid White",
     "url": "https://licenta.aiwizz.ro/product/unitate-interna-pentru-aer-conditionat-mitsubishi-ln-9000-btu-clasa-a-a-solid-white/"},
    {"title": "Aparat de aer conditionat inverter, Mitsubish, 12.000 BTU, Clasa A+++/A++, Alb",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-inverter-mitsubish-12-000-btu-clasa-a-a-alb/"},
    {"title": "Aparat de aer conditionat inverter, Mitsubishi, Electric MSZ-EF50VGKS/MUZ-EF50VG Kirigamine Zen, 18.000 BTU, Clasa A++/A+, 30 dB, Freon R32, Alb",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-inverter-mitsubishi-electric-msz-ef50vgks-muz-ef50vg-kirigamine-zen-18-000-btu-clasa-a-a-30-db-freon-r32-alb/"},
    {"title": "Aparat de aer conditionat Mitsubishi Electric MSZ-LN25VGR/MUZ-LN25VG, Inverter, 9000 BTU, Ruby Red",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-mitsubishi-electric-msz-ln25vgr-muz-ln25vg-inverter-9000-btu-ruby-red/"},
    {"title": "Aparat de aer conditionat hiperinverter, Mitsubishi Electric MSZ-LN50VGR/MUZ-LN50VG Ruby Red, 18.000 BTU, Clasa A+++/A++, 27 dB, Freon R32",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-hiperinverter-mitsubishi-electric-msz-ln50vgr-muz-ln50vg-ruby-red-18-000-btu-clasa-a-a-27-db-freon-r32/"},
    {"title": "Aparat de aer conditionat inverter, Mitsubishi Electric MSZ-EF25VGKS/MUZ-EF25VG Kirigamine Zen, 9.000 BTU, Clasa A+++/A++, 19 dB, Freon R32",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-inverter-mitsubishi-electric-msz-ef25vgks-muz-ef25vg-kirigamine-zen-9-000-btu-clasa-a-a-19-db-freon-r32/"},
    {"title": "Aer conditionat Mitsubishi Electric MSZ-AP25VG / MUZ-AP25VG R32, Inverter, 9000 BTU/h, Clasa A+++, Filtru anti-praf, Functie Econo Cool, Timer Saptamanal, Auto-restart, Wi-Fi Ready",
     "url": "https://licenta.aiwizz.ro/product/aer-conditionat-mitsubishi-electric-msz-ap25vg-muz-ap25vg-r32-inverter-9000-btu-h-clasa-a-filtru-anti-praf-functie-econo-cool-timer-saptamanal-auto-restart-wi-fi-ready/"},
    {"title": "Aer conditionat Mitsubishi Electric MSZ-DW25VF / MUZ-DW25VF R32, Kit de instalare inclus, Inverter, 9000 BTU/h, Clasa A++",
     "url": "https://licenta.aiwizz.ro/product/aer-conditionat-mitsubishi-electric-msz-dw25vf-muz-dw25vf-r32-kit-de-instalare-inclus-inverter-9000-btu-h-clasa-a/"},
    {"title": "Aer conditionat Mitsubishi Electric MSZ-HR35VF / MUZ-HR35VF R32, Wi-Fi inclus, Inverter, 12000 BTU/h, Clasa A++, Filtru anti-praf, Functie Econo Cool, Timer Saptamanal, Auto-restart",
     "url": "https://licenta.aiwizz.ro/product/aer-conditionat-mitsubishi-electric-msz-hr35vf-muz-hr35vf-r32-wi-fi-inclus-inverter-12000-btu-h-clasa-a-filtru-anti-praf-functie-econo-cool-timer-saptamanal-auto-restart/"},
    {"title": "Aer conditionat Mitsubishi Electric MSZ-EF25VEB Kirigamine Zen Negru, Inverter, 9000 BTU/h, Clasa A+++, Wi-Fi Ready",
     "url": "https://licenta.aiwizz.ro/product/aer-conditionat-mitsubishi-electric-msz-ef25veb-kirigamine-zen-negru-inverter-9000-btu-h-clasa-a-wi-fi-ready/"},
    {"title": "Aparat de aer conditionat Mitsubishi 18000 BTU Wi-Fi, Clasa A++, Quiet Comfort, High Energy-Savings, V Blocking Filter, Stylish Line-up, Kirigamine Zen MSZ-EF50VGKS, argintiu",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-mitsubishi-18000-btu-wi-fi-clasa-a-quiet-comfort-high-energy-savings-v-blocking-filter-stylish-line-up-kirigamine-zen-msz-ef50vgks-argintiu/"},
    {"title": "Aer Conditionat Mitsubishi Kirigamine Style MSZ-LN60VGV / MUZ-LN60VG, 22000 BTU, Inverter, Wi-Fi, Clasa A++, Pearl White",
     "url": "https://licenta.aiwizz.ro/product/aer-conditionat-mitsubishi-kirigamine-style-msz-ln60vgv-muz-ln60vg-22000-btu-inverter-wi-fi-clasa-a-pearl-white/"},
    {"title": "Aparat de aer conditionat Mitsubishi 9000 BTU Wi-Fi, Clasa A+++, Quiet Comfort, High Energy-Savings, V Blocking Filter, Stylish Line-up, Kirigamine Zen MSZ-EF25VGKS, argintiu",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-mitsubishi-9000-btu-wi-fi-clasa-a-quiet-comfort-high-energy-savings-v-blocking-filter-stylish-line-up-kirigamine-zen-msz-ef25vgks-argintiu/"},
    {"title": "Aer Conditionat Mitsubishi Kirigamine Style MSZ-LN60VGB / MUZ-LN60VG, 22000 BTU, Inverter, Wi-Fi, Clasa A++, Negru",
     "url": "https://licenta.aiwizz.ro/product/aer-conditionat-mitsubishi-kirigamine-style-msz-ln60vgb-muz-ln60vg-22000-btu-inverter-wi-fi-clasa-a-negru/"},
    {"title": "Aparate de aer conditionat Mitsubishi Electric MSZ-HR50VF 18000 BTU, Clasa A++, filtru anti-praf, functie Econo Cool, alb",
     "url": "https://licenta.aiwizz.ro/product/aparate-de-aer-conditionat-mitsubishi-electric-msz-hr50vf-18000-btu-clasa-a-filtru-anti-praf-functie-econo-cool-alb/"},
    {"title": "Aparate de aer conditionat Mitsubishi Electric MSZ-HR35VF 12000 BTU, Clasa A++, filtru anti-praf, functie Econo Cool, alb",
     "url": "https://licenta.aiwizz.ro/product/aparate-de-aer-conditionat-mitsubishi-electric-msz-hr35vf-12000-btu-clasa-a-filtru-anti-praf-functie-econo-cool-alb/"},
    {"title": "Aer conditionat Mitsubishi Electric MSZ-DW35VF / MUZ-DW35VF R32, Kit de instalare inclus, Inverter, 12000 BTU/h, Clasa A++, Filtru de purificare a aerului, Functie Econo Cool, Timer Saptamanal, Auto-restart, Wi-Fi Ready",
     "url": "https://licenta.aiwizz.ro/product/aer-conditionat-mitsubishi-electric-msz-dw35vf-muz-dw35vf-r32-kit-de-instalare-inclus-inverter-12000-btu-h-clasa-a-filtru-de-purificare-a-aerului-functie-econo-cool-timer-saptamanal-auto-r/"},
    {"title": "Aparat de aer conditionat Mitsubishi 12000 BTU Wi-Fi, Clasa A+++, Quiet Comfort, High Energy-Savings, V Blocking Filter, Stylish Line-up, Kirigamine Zen MSZ-EF35VGKB, negru",
     "url": "https://licenta.aiwizz.ro/product/aparat-de-aer-conditionat-mitsubishi-12000-btu-wi-fi-clasa-a-quiet-comfort-high-energy-savings-v-blocking-filter-stylish-line-up-kirigamine-zen-msz-ef35vgkb-negru/"},
    {"title": "Unitate interna pentru aer conditionat, Mitsubishi LN, 9000 BTU, Clasa A+++/A+++, Ruby Red",
     "url": "https://licenta.aiwizz.ro/product/unitate-interna-pentru-aer-conditionat-mitsubishi-ln-9000-btu-clasa-a-a-ruby-red/"},
    {"title": "Unitate interna pentru aer conditionat, Mitsubishi LN, 12000 BTU, Clasa A+++/A+++, Pearl White",
     "url": "https://licenta.aiwizz.ro/product/unitate-interna-pentru-aer-conditionat-mitsubishi-ln-12000-btu-clasa-a-a-pearl-white/"},
    {"title": "Unitate interna pentru aer conditionat, Mitsubishi HR, 14000 BTU, MSZ-HR42,Clasa A++/A++",
     "url": "https://licenta.aiwizz.ro/product/unitate-interna-pentru-aer-conditionat-mitsubishi-hr-14000-btu-msz-hr42clasa-a-a/"},
]

#links_text = "\n".join([f"{link['title']}: {link['url']}" for link in links])
#links_html = "\n".join([f'<a href="{link["url"]}">{link["title"]}</a>' for link in links])
links_text = "\n".join([f'<a href="{link["url"]}">{link["title"]}</a>' for link in links])
links_html = "<br>".join([f'<a href="{link["url"]}" target="_blank">{link["title"]}</a>' for link in links])



@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses[::-1]})

chat_log = [{"role":"system",
             "content":"Your name is Nea Gicu. You are a technical chatbot and a sales representative that helps users that arrive on our website to make better decisions \
             about buying air conditioning equipment. Please help users with clear instructions on how to use and buy our products from OUR website - aiwizz.ro. \
             Do not send or reccommend users to buy products from other websites. Do not offer links in response. Please respond in Romanian language. If you do not know how to answer a question, say: Nu va pot raspunde la aceasta intrebare, \
             dar va pot recomanda unui coleg uman din cadrul departamentului Suport si acesta va va raspunde solicitarii dvs. Multumesc! \
            Here is some additional information from our documents: {pdf_text}. \nHere are some useful links for specific questions about products and prices: {links_html}"

            }]




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
    #chat_responses.append(f"ChatBot: {bot_response}")
    #chat_responses.append(f"ChatBot: {Markup(bot_response)}") #afisare corecta linkuri
    chat_responses.append(Markup(f"ChatBot: {bot_response}"))

    # inversez ordinea mesajelor pentru afișare
    chat_contents = chat_responses[::-1]

    # obtinere data si ora curenta pentru fisierul log
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # obtin adresa IP a serverului ce afiseaza chatbot-ul
    server_host = request.client.host

    # obtin adresa IP a utilizatorului ce foloseste chatbot-ul
    client_host = request.headers.get('x-forwarded-for', request.client.host)

    # salvare conversatie in fișier text, pentru analize ulterioare
    with open("conversation_logs.txt", "a") as log_file:
        log_file.write(f"Date: {current_time}, IP Client: {client_host}, IP Server: {server_host}\n")
        for entry in chat_log:
            role = entry["role"].capitalize()
            content = entry["content"]
            log_file.write(f"{role}: {content}\n")
        log_file.write("\n" + "-" * 50 + "\n\n")  # delimitator intre conversatii

    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_contents})

@app.get("/image", response_class=HTMLResponse)
async def image(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})

@app.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, user_input: Annotated[str, Form()]):
    response = openai.Image.create(
        prompt=user_input,
        n=1,
        size="512x512"
    )
    image_url = response["data"][0]["url"]
    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)

