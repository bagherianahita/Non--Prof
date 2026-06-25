# St. John's Volunteer Hub (Prototype)

**NLP-powered volunteer–opportunity matching** prototype for nonprofit coordination in St. John's, NL.
<img width="1151" height="685" alt="image" src="https://github.com/user-attachments/assets/b55e88d3-7c4a-409b-ab24-cdd345614dae" />

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

## Quick start

```bash
pip install -r requirements.txt
python app.py
```

Open **http://localhost:5000** — browser demo with volunteer presets. Optional NLP: `python -m spacy download en_core_web_sm`

| | URL |
|---|-----|
| **Web UI (demo)** | http://localhost:5000 |
| **Health check** | http://localhost:5000/health |
| **Match API** | `POST http://localhost:5000/api/match` |

---

## License

MIT — see [LICENSE](LICENSE).
