from flask import Flask, render_template, request
import re
from collections import Counter

app = Flask(__name__)


STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then",
    "is", "are", "was", "were", "be", "been", "being",
    "to", "of", "in", "on", "for", "with", "as", "by",
    "at", "from", "this", "that", "these", "those",
    "it", "its", "i", "you", "he", "she", "we", "they",
    "my", "your", "his", "her", "our", "their",
    "have", "has", "had", "do", "does", "did",
    "will", "would", "can", "could", "should", "may",
    "might", "not", "so", "than", "too", "very",
    "into", "about", "over", "after", "before",
    "during", "through", "also"
}


def extract_keywords(text, limit=15):
    words = re.findall(r"\b[a-zA-Z][a-zA-Z'-]*\b", text.lower())

    filtered_words = [
        word for word in words
        if word not in STOP_WORDS and len(word) > 2
    ]

    word_frequency = Counter(filtered_words)

    keywords = [
        {"word": word, "frequency": frequency}
        for word, frequency in word_frequency.most_common(limit)
    ]

    return keywords


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    keywords = []

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if text:
            keywords = extract_keywords(text)

    return render_template(
        "index.html",
        text=text,
        keywords=keywords
    )


if __name__ == "__main__":
    app.run(debug=True)
