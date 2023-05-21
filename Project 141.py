from flask import Flask, jsonify, request
import csv

all_articles = []

app = Flask(__name__)

with open("articles.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

@app.route("/get_article")
def get_article():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success!"
    })


@app.route("/liked_article", methods = ["POST"])
def liked_article():
    article = all_articles[0]
    liked_article.append(article)
    all_articles.pop(0)
    return jsonify({
        "status" : "success!"
    })

@app.route("/not_liked_article", methods=["POST"])
def not_liked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status" : "success!"
    })

if __name__ == "__main__":
    app.run()