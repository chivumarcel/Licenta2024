# import openai
# from openai import OpenAI
# import gradio as gr
# import PyPDF2
# import os
# from dotenv import load_dotenv
#
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = api_key  # setez cheia API global
#
# # client = OpenAI(api_key=api_key)
# def predict(message, history):
#     history_openai_format = []
#     for human, assistant in history:
#         history_openai_format.append({"role": "user", "content": human})
#         history_openai_format.append({"role": "assistant", "content": assistant})
#     history_openai_format.append({"role": "user", "content": message})
#
#     response = client.chat.completions.create(model='gpt-3.5-turbo',
#                                               messages=history_openai_format,
#                                               temperature=1.0,
#                                               stream=True)
#     partial_message = ""
#     for chunk in response:
#         if chunk.choices[0].delta.content is not None:
#             partial_message = partial_message + chunk.choices[0].delta.content
#             yield partial_message
#
# #gr.ChatInterface(predict).launch()
# gr.ChatInterface(predict).launch(share=True)
#
# def extract_text_from_pdf(file_path):
#     pdf_file = open(file_path, 'rb')
#     reader = PyPDF2.PdfFileReader(pdf_file)
#     text = ""
#     for page in range(reader.numPages):
#         text += reader.getPage(page).extractText()
#     pdf_file.close()
#     return text
# #definim o lista goala simpla
# history = []
#
# # folosim textul extras ca mesaj sau istoric in functia de predictie
# message = extract_text_from_pdf('assets/WF-RAC-USER’S MANUAL_english.pdf')
# predict(message, history)

import openai
import gradio as gr
import PyPDF2
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # Setează cheia API global

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    # apelare API-ul folosind direct biblioteca openai
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=history_openai_format,
        temperature=1.0,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta and chunk.choices[0].delta.content is not None:
            partial_message += chunk.choices[0].delta.content
            yield partial_message

# interfata Gradio cu generatorul
iface = gr.Interface(
    fn=predict,
    inputs=["text", "state"],
    outputs=["text", "state"],
    allow_flagging="never",
    title="Chatbot with GPT-3.5 Turbo",
    description="A chatbot using GPT-3.5 Turbo through the OpenAI API."
)

if __name__ == "__main__":
    iface.launch(share=True)

def extract_text_from_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page in range(reader.numPages):
        text += reader.getPage(page).extractText()
    pdf_file.close()
    return text

# definire lista pentru istoric
history = []

# utilizare text extras ca mesaj sau istoric in predictie
message = extract_text_from_pdf('assets/WF-RAC-USER’S MANUAL_english.pdf')
predict(message, history)
