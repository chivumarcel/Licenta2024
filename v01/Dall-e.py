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

#openai = OpenAI(api_key=api_key)

response = openai.Image.create(
    prompt="generate a duck with glasses staying on a lake in a mountains area, photorealistic",
    n = 1,
    size = "1024x1024"
)
print(response["data"][0]["url"])
#image_url = response.data[0].url