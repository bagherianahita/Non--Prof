# St. John's Volunteer Hub (Prototype)

**NLP-powered volunteer–opportunity matching** prototype for nonprofit coordination in St. John's, NL.

![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?style=flat-square)

---

## Architecture (roadmap)

```
┌──────────────┐   skills NLP  ┌──────────────┐   match    ┌──────────────┐
│ Volunteers   │ ────────────► │  Flask API   │ ─────────► │ Opportunities│
│ (profiles)   │               │  + spaCy     │            │ (nonprofits) │
└──────────────┘               └──────────────┘            └──────────────┘
                                      ▲
                               ┌──────┴───────┐
                               │ React UI     │  (planned)
                               └──────────────┘
```

> **Runnable demo:** `app.py` (Flask API). The Jupyter notebook is exploratory only.

---

## Quick start (employers — no API keys)

```bash
pip install -r requirements.txt
python app.py
```

```bash
curl -X POST http://localhost:5000/api/match -H "Content-Type: application/json" -d "{}"
```

Empty `{}` uses default skills/interests. Or send: `{"skills":"social media","interests":"youth mental health"}`

| | URL |
|---|-----|
| **API** | http://localhost:5000 |
| **Health check** | http://localhost:5000/health |
| **Match endpoint** | `POST http://localhost:5000/api/match` |

---

## License

MIT — see [LICENSE](LICENSE).
