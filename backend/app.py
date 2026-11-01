from flask import Flask, jsonify, send_from_directory
from pathlib import Path

app = Flask(__name__)

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# Maximum request size: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


# Home route
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


# Health check API
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "ResumeIQ backend is running!",
        "version": "1.0.0"
    }), 200


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True, port=5000)