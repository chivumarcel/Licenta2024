import openai
# from openai import OpenAI #this is not working as 28th of June 2024
import os
from dotenv import load_dotenv #in order to use the api key from .env
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # set API key

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

chat_log = [{"role":"system",
             "content":"you are a technical chatbot that helps users that arrive on our website to make better decisions \
             about air conditioning equipment. Please help users with clear instructions on how to use and buy our products. \
             Please respond in Romanian language. If you do not know how to answer a question, say: Nu va pot raspunde la aceasta intrebare, \
             dar va pot recomanda unui coleg uman din cadrul departamentului Suport si acesta va va raspunde solicitarii dvs. Multumesc!"

            }]



@app.post("/")
async def chat(user_input: Annotated[str, Form()]):
    chat_log.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
    #response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        temperature=0.5
    )

    bot_response = response["choices"][0]["message"]["content"]
    # bot_response = response.choices[0].message['content']
    # bot_response = response.choices[0].message.content.strip()

    chat_log.append({"role":"assistant", "content":bot_response})
    return bot_response


