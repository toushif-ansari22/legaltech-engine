import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """PDF se page by page text nikalta hai"""
    doc = fitz.open(pdf_path)
    full_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()

        # Clean karo — extra spaces aur broken lines hatao
        text = text.strip()
        text = " ".join(text.split())

        full_text += f"\n--- Page {page_num + 1} ---\n{text}"

    doc.close()
    return full_text


def split_into_paragraphs(text):
    """Text ko paragraphs mein tod do"""
    paragraphs = text.split("\n")
    # Empty paragraphs hatao
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return paragraphs