import openai
import gradio as gr

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # setez cheia API global

def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content']

# Crearea interfeței cu Gradio
iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="Chatbot Antrenat cu GPT-3.5 Turbo",
    description="Un chatbot folosind GPT-3.5 Turbo prin OpenAI API"
)

if __name__ == "__main__":
    iface.launch(share=True)
