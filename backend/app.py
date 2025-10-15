from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models import db
from routes.auth_routes import auth_bp
# from routes.ai_routes import ai_bp  # Temporarily commented for Phase A testing


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    jwt = JWTManager(app)

    # --- Add this block ---
    from routes.auth_routes import revoked_tokens

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return jti in revoked_tokens
    # ----------------------

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    # app.register_blueprint(ai_bp, url_prefix="/api/ai")  # Will be enabled in Phase C

    @app.route("/")
    def home():
        return jsonify({
            "message": "AI Study Assistant API running",
            "version": "1.0.0",
            "status": "Phase A - Scaffolding Complete"
        })

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=Config.FLASK_DEBUG, host="127.0.0.1", port=5000)
