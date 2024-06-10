from flask import Flask, request, jsonify
import openai

from v02.ExtractData import cleaned_texts

app = Flask(__name__)
openai.api_key = '##'

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    context = " ".join(cleaned_texts)
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=f"{context}\n\nUser: {user_input}\nBot:",
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(port=5000)
