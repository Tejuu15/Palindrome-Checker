import re

from flask import Flask, render_template, request

app = Flask(__name__)


def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    result = None

    if request.method == "POST":
        text = request.form.get("text", "")
        result = is_palindrome(text)

    return render_template("index.html", text=text, result=result)


if __name__ == "__main__":
    app.run(debug=True)