"""St. John's Volunteer Hub — Flask API with NLP opportunity matching."""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
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


def _load_nlp():
    try:
        import spacy
    except ImportError:
        return None
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        from spacy.cli import download

        download("en_core_web_sm")
        import spacy

        return spacy.load("en_core_web_sm")


nlp = _load_nlp()


def _score(volunteer_text: str, description: str) -> float:
    if nlp is None:
        words = set(volunteer_text.lower().split())
        desc = set(description.lower().split())
        overlap = len(words & desc)
        return round(min(0.95, 0.3 + overlap * 0.1), 2)
    v_doc = nlp(volunteer_text)
    o_doc = nlp(description)
    return round(float(v_doc.similarity(o_doc)), 2)


@app.get("/health")
def health():
    return {"status": "ok", "opportunities": len(OPPORTUNITIES)}


@app.post("/api/match")
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
    print("Volunteer Hub API — demo defaults: skills=communication leadership, interests=environment community")
    print("POST http://localhost:5000/api/match  with JSON body or empty {} for defaults")
    app.run(host="0.0.0.0", port=5000, debug=True)
