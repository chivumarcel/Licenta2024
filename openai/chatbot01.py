import openai
# from openai import OpenAI #this is not working as 28th of June 2024
import os
from dotenv import load_dotenv #in order to use the api key from .env

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # set API key

chat_log = []

while True:
    user_input = input()
    if user_input.lower() == "stop":
        break
    chat_log.append({"role":"user", "content":user_input})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        temperature=0.5
    )
#bot_response = response["choices"][0]["message"]["content"]
bot_response = response.choices[0].message.content

chat_log.append({"role":"assistant", "content":bot_response})
print("Bot:", bot_response)

# response = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     # messages=[
#     #     {
#     #         "role":"system",
#     #         "content":"Esti un asistent virual industrial, \
#     #         cu scopul de a ajuta utilizatorii sa inteleaga cat mai bine specificatiile tehnice pentru aparatele de aer conditionat \
#     #         si echipamentele comercializate pe site-ul AIWIZZ"
#     #     },
#     #     {
#     #         "role":"user",
#     #         "content":"cum pot instala un aparat de aer conditionat"
#     #     }
#     # ]
#     messages=[
#         {
#             "role": "system",
#             "content": "You are the CEO of Apple"
#         },
#         {
#             "role":"assistant",
#             "content": "iPhone is awesome piece of tech"
#         },
#         {
#             "role": "user",
#             "content": "What year was released more precisely"
#         }
#     ],
#     temperature=0.5
# )
# print(response)
# print(response.choices[0].message.content)
