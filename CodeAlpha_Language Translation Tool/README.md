## &nbsp;**🌍 Language Translation \& Speech Tool**



This is my internship project: a **Flask-based translation tool** with **Text-to-Speech (TTS)** integration.  

It uses **Dockerized LibreTranslate** as backend for offline translations and integrates **gTTS/pyttsx3** for speech playback in the browser.



---



#### **✨ Features**

\- Translate between **English, French, Arabic, Urdu**

\- Copy translated text to clipboard

\- Speak translated text directly in browser

\- Modern UI with Flask + HTML/CSS/JS

\- Dockerized backend for reproducibility



---



#### **🛠️ Tech Stack**

\- \*\*Backend\*\*: Python, Flask, LibreTranslate (Docker)

\- \*\*Frontend\*\*: HTML, CSS, JavaScript

\- \*\*Speech\*\*: gTTS (MP3, browser playback), pyttsx3 (local fallback)

\- \*\*Containerization\*\*: Docker



---



#### **📂 Project Structure**

```

Translation Tool/

│── app.py              # Flask app

│── requirements.txt    # Python dependencies

│── Dockerfile          # Container setup

│── templates/

│    └── index.html     # Frontend UI

│── static/

│    ├── style.css      # Styling

│    └── script.js      # JS logic (copy + speak)

│── README.md           # Documentation

```



---

### 

### **⚡ Setup Instructions**



##### **1. Install Dependencies**



*requirements.txt*

<b>Flask</b>

<b>requests</b>

<b>pyttsx3</b>

<b>gTTS</b>



```**bash**

pip install -r requirements.txt

```

##### 

##### **2. Run LibreTranslate in Docker**

```**bash**

docker run -it -p 5000:5000 libretranslate/libretranslate

```



##### **3. Start Flask App**

```**bash**

python app.py

```



##### **4. Open in Browser**

```

http://127.0.0.1:8000

```



---

##### 

##### **🔊 Text-to-Speech Notes**

\- **gTTS** → generates MP3 (works in browser, supports Urdu/Arabic)

\- **pyttsx3** → local fallback (WAV, system voices)



---



##### **🧪 Example**

\- **Input**: `"Hello World"`

\- **Source**: `en`

\- **Target**: `fr`

\- **Output**: `"Bonjour le monde"`

\- Click **Speak** → browser plays French audio 🎙️



---



##### **🚀 Future Improvements**

\- Add more languages

\- Deploy on cloud (Heroku/DockerHub)

\- Enhance UI with React/Vue





