"""St. John's Volunteer Hub — Flask API + browser matching demo."""

from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

STATIC_DIR = Path(__file__).parent / "static"
DEFAULT_PORT = 5000

app = Flask(__name__, static_folder=str(STATIC_DIR))
CORS(app)

OPPORTUNITIES = [
    {
        "id": 1,
        "title": "Beach Cleanup Crew Leader",
        "description": "Lead volunteers for coastal cleanups. Organizational and communication skills. Environmental conservation interest.",
        "organization": "Conservation Corps NL",
    },
    {
        "id": 2,
        "title": "Social Media Coordinator",
        "description": "Manage social channels for youth mental health awareness. Instagram and TikTok experience.",
        "organization": "Choices for Youth",
    },
    {
        "id": 3,
        "title": "Kitchen Helper",
        "description": "Food prep and serving at community kitchen. Basic cooking skills helpful.",
        "organization": "Stella's Circle",
    },
]

_nlp = None


def _get_nlp():
    global _nlp
    if _nlp is not None:
        return _nlp
    try:
        import spacy

        try:
            _nlp = spacy.load("en_core_web_sm")
        except OSError:
            _nlp = None
    except ImportError:
        _nlp = None
    return _nlp


def _score(volunteer_text: str, description: str) -> float:
    nlp = _get_nlp()
    if nlp is None:
        words = set(volunteer_text.lower().split())
        desc_words = set(description.lower().split())
        overlap = len(words & desc_words)
        return round(min(0.95, 0.35 + overlap * 0.12), 2)
    v_doc = nlp(volunteer_text)
    o_doc = nlp(description)
    return round(float(v_doc.similarity(o_doc)), 2)


@app.route("/")
def demo_ui():
    demo_path = STATIC_DIR / "demo.html"
    if demo_path.exists():
        return send_from_directory(STATIC_DIR, "demo.html")
    return jsonify({"message": "Volunteer Hub API", "health": "/health", "match": "POST /api/match"})


@app.route("/health")
def health():
    return jsonify({"status": "ok", "opportunities": len(OPPORTUNITIES), "nlp": _get_nlp() is not None})


@app.route("/api/match", methods=["POST"])
def match_opportunities():
    data = request.get_json(silent=True) or {}
    skills = (data.get("skills") or "communication leadership").strip()
    interests = (data.get("interests") or "environment community").strip()
    volunteer_text = f"{skills} {interests}"

    matches = []
    for opp in OPPORTUNITIES:
        score = _score(volunteer_text, opp["description"])
        matches.append({"opportunity": opp, "relevance_score": score})
    matches.sort(key=lambda m: m["relevance_score"], reverse=True)
    return jsonify(matches)


if __name__ == "__main__":
    print(f"Volunteer Hub: http://localhost:{DEFAULT_PORT}")
    print("Browser demo with presets — optional: python -m spacy download en_core_web_sm")
    app.run(host="127.0.0.1", port=DEFAULT_PORT, debug=False)
