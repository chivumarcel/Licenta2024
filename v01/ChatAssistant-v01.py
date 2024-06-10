from openai import OpenAI
import gradio
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)



messages = [{"role": "system", "content": "You are a chatbot consultant that offers personalized advice to customers. "
                                          "You will provide personalized feedback from a dataset of files that I will provide."
                                          "Please response in a polite manner, in Romanian language. "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model = "gpt-3.5-turbo",
    messages = messages)
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Nea Gică")

demo.launch(share=True)