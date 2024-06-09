import openai
import gradio as gr

# configurare cheie API
openai.api_key = 'sk-proj-mcgXgPyztA6SH11UGkcCT3BlbkFJqECpgt5wEm3Ri6e1WqhA'

def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content']

# crearea interfetei cu gradio
iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="Chatbot Antrenat cu GPT-3.5 Turbo",
    description="Un chatbot folosind GPT-3.5 Turbo prin OpenAI API"
)

if __name__ == "__main__":
    iface.launch(share=True)
