from flask import Flask, render_template, request, jsonify

# import chatbot logic
from python_faq_chatbot import get_best_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message") if data else ""
    reply = get_best_answer(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
