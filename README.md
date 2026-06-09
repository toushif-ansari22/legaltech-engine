# LegalTech - Automated Contract Parsing & Risk Extraction Engine

> Automatically reads PDF contracts and flags high-risk legal clauses using NLP.

## Problem Statement
Law firms manually review thousands of NDAs and MSAs every year. This system reduces contract review time by 70% using Python + NLP.

## Features
- Upload PDF contracts via REST API
- Extract text page by page using PyMuPDF
- Identify company names, dates & locations using spaCy NLP
- Flag risky clauses — "indemnify", "unlimited liability", "exclusive"
- Store results with risk levels in database
- Admin dashboard for non-technical users

## Tech Stack
| Component | Technology |
|-----------|------------|
| Backend | Python, Django, DRF |
| PDF Processing | PyMuPDF (Fitz) |
| NLP Engine | spaCy |
| Database | SQLite |

## Setup Instructions

```bash
pip3 install django djangorestframework pymupdf spacy
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/documents/ | List all documents |
| POST | /api/documents/upload/ | Upload PDF contract |

## Admin Panel
http://127.0.0.1:8000/admin/

## Weekly Progress
- Week 1 — Django setup, models, API endpoints
- Week 2 — PDF text extraction using PyMuPDF
- Week 3 — NLP integration, entity extraction, risk flagging
- Week 4 — Nested JSON serialization, admin dashboard, README
