import openai #update 14.07.2024, 13:00+, v03
import os
from dotenv import load_dotenv #in order to use the api key from .env
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # set API key via .env file

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

chat_log = [{"role":"system",
             "content":"Your name is Nea Gicu. You are a technical chatbot that helps users that arrive on our website to make better decisions \
             about air conditioning equipment. Please help users with clear instructions on how to use and buy our products. \
             Please respond in Romanian language. If you do not know how to answer a question, say: Nu va pot raspunde la aceasta intrebare, \
             dar va pot recomanda unui coleg uman din cadrul departamentului Suport si acesta va va raspunde solicitarii dvs. Multumesc!"

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



