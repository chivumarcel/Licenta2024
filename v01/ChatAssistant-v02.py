from openai import OpenAI
import gradio as gr
import PyPDF2

api_key = "sk-proj-mcgXgPyztA6SH11UGkcCT3BlbkFJqECpgt5wEm3Ri6e1WqhA"  #
client = OpenAI(api_key=api_key)
def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(model='gpt-3.5-turbo',
                                              messages=history_openai_format,
                                              temperature=1.0,
                                              stream=True)
    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message

#gr.ChatInterface(predict).launch()
gr.ChatInterface(predict).launch(share=True)

def extract_text_from_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page in range(reader.numPages):
        text += reader.getPage(page).extractText()
    pdf_file.close()
    return text
#definim o lista goala simpla
history = []

# folosim textul extras ca mesaj sau istoric in functia de predictie
message = extract_text_from_pdf('assets/WF-RAC-USER’S MANUAL_english.pdf')
predict(message, history)
