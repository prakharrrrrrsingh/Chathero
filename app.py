import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI  # ✅ NEW import method for openai>=1.0.0

load_dotenv()

# ✅ Initialize the client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")  # OpenRouter base
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get("msg")
    try:
        # ✅ New ChatCompletion method
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[{"role": "user", "content": user_message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
