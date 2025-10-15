from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with summaries
    summaries = db.relationship(
        "Summary", backref="user", lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        """Convert User object to dictionary for API responses"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }


class Summary(db.Model):
    __tablename__ = "summaries"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(200), nullable=False,
                      default="Untitled Summary")

    # Content with 10,000 character limit constraint
    content = db.Column(db.Text(10000), nullable=False)  # Original text input
    summary = db.Column(db.Text, nullable=True)  # AI-generated summary
    flashcards = db.Column(db.JSON, nullable=True)  # Generated flashcards

    # Metadata
    # Word count of original content
    word_count = db.Column(db.Integer, default=0)
    # Time taken to process (seconds)
    processing_time = db.Column(db.Float, default=0.0)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self, include_content=False):
        """Convert Summary object to dictionary for API responses"""
        result = {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "summary": self.summary,
            "flashcards": self.flashcards,
            "word_count": self.word_count,
            "processing_time": self.processing_time,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

        if include_content:
            result["content"] = self.content

        return result

    def to_preview_dict(self):
        """Convert Summary to preview format for listing"""
        summary_preview = self.summary[:100] + "..." if self.summary and len(
            self.summary) > 100 else self.summary
        return {
            "id": self.id,
            "title": self.title,
            "summary_preview": summary_preview,
            "word_count": self.word_count,
            "flashcard_count": len(self.flashcards) if self.flashcards else 0,
            "created_at": self.created_at.isoformat()
        }
