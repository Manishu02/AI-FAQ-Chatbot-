import sqlite3
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load AI Modelgit init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin https://github.com/Manishu02/AI-FAQ-Chatbot 

git push -u origin main
model = SentenceTransformer("all-MiniLM-L6-v2")

# NLTK
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess(text):
    words = word_tokenize(text.lower())

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word.isalnum() and word not in stop_words
    ]

    return " ".join(words)


def get_answer(user_question):

    conn = sqlite3.connect("faq.db")
    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM faq")
    data = cursor.fetchall()

    processed_user = preprocess(user_question)

    user_embedding = model.encode(processed_user, convert_to_tensor=True)

    best_answer = None
    best_score = 0

    for question, answer in data:

        processed_question = preprocess(question)

        question_embedding = model.encode(
            processed_question,
            convert_to_tensor=True
        )

        score = util.cos_sim(
            user_embedding,
            question_embedding
        ).item()

        if score > best_score:
            best_score = score
            best_answer = answer

    if best_score >= 0.50:

        cursor.execute(
            """
            INSERT INTO logs(question, answer)
            VALUES (?, ?)
            """,
            (user_question, best_answer)
        )

        conn.commit()
        conn.close()

        return best_answer

    answer = "Sorry, I don't know the answer."

    cursor.execute(
        """
        INSERT INTO logs(question, answer)
        VALUES (?, ?)
        """,
        (user_question, answer)
    )

    conn.commit()
    conn.close()

    return answer