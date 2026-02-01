## **Python FAQ Chatbot 🤖**



A simple chatbot built with Python, **NLTK**, and **TF‑IDF vectorization** that answers frequently asked questions (FAQs) about Python.  

The bot uses text preprocessing, synonym mapping, and cosine similarity to match user queries against a curated FAQ dataset.  

It can run both interactively in the terminal and as a **Flask web app** with a browser-based interface.



---



##### **🚀 Features**

\- Loads FAQs from a CSV file (`Question`, `Answer`).

\- Preprocesses text with:

&nbsp; - Tokenization, stopword removal, lemmatization.

&nbsp; - Synonym mapping (e.g., **introduced → released**).

\- Encodes questions using **TF‑IDF**.

\- Finds the most relevant answer using **cosine similarity.**

\- Includes a confidence threshold to avoid random answers.

\- Supports two modes:

&nbsp; - **Terminal mode** → interactive Q\&A.

&nbsp; - **Web mode** → Flask app with `/chat` endpoint and HTML frontend.



---

##### 

##### **📊 Dataset**

The dataset is stored in a CSV file with two columns:



```**csv**

Question,Answer



What is Python?,A high-level, interpreted programming language.

Who created Python?,Guido van Rossum.

When was Python first released?,1991.

```



You can expand these datasets (e.g., `164 FAQs`, `51 FAQs`) by adding more rows.



---



##### **🖥️ Usage**



**1. Terminal Mode**

Run the chatbot directly:

```**bash**

python python\_faq\_chatbot.py

```



**Example interaction:**

```

FAQ Chatbot ready! Type 'exit' to quit.

You: Who created Python?

Bot: Guido van Rossum.

```



---



**2. Web Mode (Flask App)**

Run the Flask server:

```**bash**

python app.py

```



This will start a local server at `http://127.0.0.1:5000/`.



\- Visit **`/`** → loads **`index.html`**.

\- Send POST requests to **`/chat`** with JSON:

```json

{

&nbsp; "message": "Who created Python?"

}

```

Response:

```json

{

&nbsp; "reply": "Guido van Rossum."

}

```



---



**📝 Structure Summary**

\- **Dataset** → `faq\_dataset.csv` with `Question,Answer`.

\- **Preprocessing** → NLTK tokenization, stopword removal, lemmatization, synonym mapping.

\- **Vectorization** → TF‑IDF fitted on preprocessed questions.

\- **Answer Retrieval** → `get\_best\_answer()` computes cosine similarity and applies confidence threshold.

\- **Interfaces:**

&nbsp; - `python\_faq\_chatbot.py` → terminal chatbot.

&nbsp; - `app.py` → Flask web app with `/chat` API and HTML frontend.





