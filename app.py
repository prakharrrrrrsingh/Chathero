from flask import Flask, request, jsonify, render_template
from openai import OpenAI  # ✅ NEW import method for openai>=1.0.0

# Directly set your API key and base URL here
OPENROUTER_API_KEY = "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"
OPENAI_BASE_URL = "https://openrouter.ai/api/v1"

# ✅ Initialize the client
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENAI_BASE_URL
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
