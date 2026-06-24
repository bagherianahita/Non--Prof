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

> **Current state:** `nonprofit.ipynb` contains a Flask + spaCy backend prototype. Full-stack React + PostgreSQL is on the roadmap.

---

## Quick start

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
jupyter notebook nonprofit.ipynb
```

---

## License

MIT — see [LICENSE](LICENSE).
