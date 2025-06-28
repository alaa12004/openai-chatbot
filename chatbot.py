from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = "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"


system_prompt = """
✅ Important instructions:
- Answer in the same language as the question (Arabic or English).
- After showing any code, explain it step by step.
- Keep the answer organized and simple, follow this structure:
  1. A short summary of the idea.
  2. Key points in brief.
  3. Code examples if needed.
  4. Line-by-line code explanation.
  5. Avoid long paragraphs.
  6. Highlight important information or key points in bold.
✅ Always answer in this format.
"""

@app.route("/chat", methods=["POST"])
def chat_api():
    try:
        user_input = request.json["message"]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response['choices'][0]['message']['content']
        return jsonify({"reply": answer})

    except Exception as e:
        return jsonify({"reply": f"Error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

