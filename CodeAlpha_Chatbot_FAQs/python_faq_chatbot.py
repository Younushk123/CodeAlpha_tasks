# Python FAQ Chatbot

import nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download once manually OR keep this guarded
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
    nltk.download("stopwords")
    nltk.download("wordnet")

#1. Load dataset

# Adjust path to your local file
df = pd.read_csv("faq_dataset.csv", encoding="latin1")

# Normalize column names to lowercase
df.columns = df.columns.str.lower()


#2. Preprocessing function

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    if not isinstance(text, str):   # handle NaN or non-string
        return ""
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens
              if word not in stop_words and word not in string.punctuation]

    # Synonym mapping for better matching
    synonyms = {"introduced":"released", "created":"released", "year":"date"}
    tokens = [synonyms.get(word, word) for word in tokens]

    return " ".join(tokens)

# Apply preprocessing
df['question'] = df['question'].fillna("").astype(str)
df['clean_question'] = df['question'].apply(preprocess)



#3. Fit TF‑IDF

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['clean_question'])


#4. Answer retrieval function

def get_best_answer(user_query):
    query_vec = vectorizer.transform([preprocess(user_query)])
    similarities = cosine_similarity(query_vec, X)
    best_idx = similarities.argmax()
    best_score = similarities.max()

    if best_score < 0.3:
        return "Sorry, I don't know the answer to that."
    return df['answer'].iloc[best_idx]

#5. Demo mode (quick test)

# print("\nFAQ Chatbot demo:")
# test_queries = [
#     "How do I create a list in Python?",
#     "What is a dictionary?",
#     "How to install a package?",
#     "Explain Python functions",
#     "What is a loop?"
# ]
# for q in test_queries:
#     print("You:", q)
#     print("Bot:", get_best_answer(q))
#     print()

#6. Interactive chatbot (VS Code only)

if __name__ == "__main__":
    print("FAQ Chatbot ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        print("Bot:", get_best_answer(user_input))


