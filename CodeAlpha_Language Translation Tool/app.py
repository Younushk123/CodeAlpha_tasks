from flask import Flask, render_template, request, send_file
import requests
from gtts import gTTS
import tempfile
import os

app = Flask(__name__)
API_URL = "http://127.0.0.1:5000/translate"

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        source_lang = request.form.get("src")
        target_lang = request.form.get("tgt")

        if text and source_lang and target_lang:
            resp = requests.post(API_URL, json={
                "q": text,
                "source": source_lang,
                "target": target_lang,
                "format": "text"
            })
            if resp.status_code == 200:
                translated_text = resp.json()["translatedText"]
            else:
                translated_text = f"Error: {resp.text}"

    return render_template("index.html", translated_text=translated_text, input_text=text)

@app.route("/speak", methods=["POST"])
def speak():
    text = request.form.get("text", "")
    if not text:
        return "No text provided", 400

    # Generate MP3 using gTTS
    tts = gTTS(text=text, lang="en")  # change lang dynamically if needed
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)
    tmp_file.close()

    response = send_file(tmp_file.name, mimetype="audio/mpeg")
    @response.call_on_close
    def cleanup():
        try:
            os.remove(tmp_file.name)
        except:
            pass
    return response

if __name__ == "__main__":
    app.run(debug=True, port=8000)
