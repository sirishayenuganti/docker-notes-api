from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_url = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(mongo_url)
db = client["notesdb"]
notes_collection = db["notes"]

@app.route("/")
def home():
    return "Notes API is running. Try POST /notes and GET /notes"

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "text field is required"}), 400
    result = notes_collection.insert_one({"text": text})
    return jsonify({"id": str(result.inserted_id), "text": text}), 201

@app.route("/notes", methods=["GET"])
def get_notes():
    notes = []
    for note in notes_collection.find():
        notes.append({"id": str(note["_id"]), "text": note["text"]})
    return jsonify(notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)