from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from transformers import pipeline
from models import db, Summary
from datetime import datetime

ai_bp = Blueprint("ai", __name__)

# Load Hugging Face model once at startup
summarizer = pipeline("summarization", model="t5-small")

def generate_flashcards(summary_text, num_cards=5):
    lines = summary_text.split(". ")
    flashcards = []
    for i, line in enumerate(lines[:num_cards]):
        if len(line.strip()) > 20:
            flashcards.append({
                "question": f"What is key point {i+1}?",
                "answer": line.strip()
            })
    return flashcards

@ai_bp.route("/generate", methods=["POST"])
@jwt_required()
def generate_summary():
    data = request.get_json()
    user_id = get_jwt_identity()
    text = data.get("text")
    title = data.get("title", "Untitled Summary")

    if not text or len(text.strip()) < 20:
        return jsonify({"error": "Please provide enough text"}), 400

    summary_result = summarizer(text, max_length=200, min_length=50, do_sample=False)
    summary_text = summary_result[0]["summary_text"]
    flashcards = generate_flashcards(summary_text)

    new_summary = Summary(
        user_id=user_id,
        title=title,
        content=text,
        summary=summary_text,
        flashcards=flashcards,
        created_at=datetime.utcnow()
    )
    db.session.add(new_summary)
    db.session.commit()

    return jsonify({
        "summary": summary_text,
        "flashcards": flashcards
    }), 200
