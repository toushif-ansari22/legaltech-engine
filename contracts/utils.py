import fitz  # PyMuPDF
import spacy

# spaCy model load karo
nlp = spacy.load("en_core_web_sm")

# Risky keywords list
RISK_KEYWORDS = [
    "indemnify", "indemnification",
    "unlimited liability", "exclusive",
    "governing law", "jurisdiction",
    "terminate", "termination",
    "confidential", "penalty"
]

def extract_text_from_pdf(pdf_path):
    """PDF se page by page text nikalta hai"""
    doc = fitz.open(pdf_path)
    full_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        text = text.strip()
        text = " ".join(text.split())
        full_text += f"\n--- Page {page_num + 1} ---\n{text}"

    doc.close()
    return full_text


def split_into_paragraphs(text):
    """Text ko paragraphs mein tod do"""
    paragraphs = text.split("\n")
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return paragraphs


def extract_entities(text):
    """spaCy se company names aur dates nikalo"""
    doc = nlp(text)
    entities = {
        "organizations": [],
        "dates": [],
        "locations": []
    }
    for ent in doc.ents:
        if ent.label_ == "ORG":
            entities["organizations"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["dates"].append(ent.text)
        elif ent.label_ == "GPE":
            entities["locations"].append(ent.text)
    return entities


def flag_risky_clauses(paragraphs):
    """Risky keywords wale paragraphs flag karo"""
    flagged = []
    for para in paragraphs:
        para_lower = para.lower()
        for keyword in RISK_KEYWORDS:
            if keyword in para_lower:
                flagged.append({
                    "text": para,
                    "keyword": keyword,
                    "risk_level": "high"
                })
                break
    return flagged