import sqlite3

from flask import Flask, render_template, request, redirect
from chatbot import get_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        user_question = request.form["question"]

        response = get_answer(user_question)

    return render_template(
        "index.html",
        response=response
    )

@app.route("/history")
def history():

    conn = sqlite3.connect("faq.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT question, answer, created_at
    FROM logs
    ORDER BY id DESC
    """)

    logs = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        logs=logs
    )

@app.route("/clear_history")
def clear_history():

    conn = sqlite3.connect("faq.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM logs")

    conn.commit()
    conn.close()

    return redirect("/history")

if __name__ == "__main__":
    app.run(debug=True)