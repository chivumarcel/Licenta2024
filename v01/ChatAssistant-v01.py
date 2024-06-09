from openai import OpenAI

client = OpenAI(api_key="sk-proj-mcgXgPyztA6SH11UGkcCT3BlbkFJqECpgt5wEm3Ri6e1WqhA")
import gradio


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