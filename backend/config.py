import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

class Config:
    # Security Keys
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")  # Change this in production
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_dev_secret")  # Change this in production
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Configuration
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 900))  # 15 minutes
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", 2592000))  # 30 days
    
    # AI Model Configuration
    TEXT_MAX_LENGTH = int(os.getenv("TEXT_MAX_LENGTH", 10000))
    AI_MODEL_NAME = os.getenv("AI_MODEL_NAME", "google/flan-t5-small")
    AI_MODEL_CACHE_DIR = os.getenv("AI_MODEL_CACHE_DIR", "./models_cache")
    
    # Application Settings
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    
    # Rate Limiting Configuration
    RATE_LIMIT_GENERATE = int(os.getenv("RATE_LIMIT_GENERATE", 10))
    RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW", 3600))
