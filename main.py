from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/api/random", methods=["GET", "POST"])
def get_random():
    if request.method == "POST":
        payload = request.get_json()
        r = requests.post("https://scibowldb.com/api/questions", json=payload)
    else:
        r = requests.get("https://scibowldb.com/api/questions")

    data = r.json()
    questions = data.get("questions", [])
    if not questions:
        return jsonify({"questions": []})

    return jsonify({"questions": [random.choice(questions)]})

app.run(host="0.0.0.0", port=8080)
