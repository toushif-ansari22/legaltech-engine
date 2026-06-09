# LegalTech - Automated Contract Parsing & Risk Extraction Engine

## Project Overview
Django-based backend that automatically parses PDF contracts and flags high-risk legal clauses using NLP.

## Tech Stack
- Python + Django + Django REST Framework
- PyMuPDF (Fitz) — PDF text extraction
- spaCy — NLP entity recognition
- SQLite (development)

## Setup Instructions

### 1. Install dependencies
pip3 install django djangorestframework pymupdf spacy

### 2. Download spaCy model
python3 -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl

### 3. Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

### 4. Create admin user
python3 manage.py createsuperuser

### 5. Start server
python3 manage.py runserver

## API Endpoints
- GET  /api/documents/         — List all documents
- POST /api/documents/upload/  — Upload PDF contract

## Admin Panel
http://127.0.0.1:8000/admin/

## Weekly Progress
- Week 1: Django setup, models, API endpoints
- Week 2: PDF text extraction using PyMuPDF
- Week 3: NLP integration, entity extraction, risk flagging
- Week 4: Nested JSON serialization, admin dashboard