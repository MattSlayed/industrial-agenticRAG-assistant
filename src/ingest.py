"""
Ingestion for both sources. Implement as you work through the roadmap.

TODO (manuals):
  - load PDFs from data/manuals/ (PyPDFLoader or similar)
  - chunk them (RecursiveCharacterTextSplitter) — think about chunk size
    relative to how specific a torque-spec-style answer needs to be
  - embed + persist to a local vector store (Chroma/FAISS)
  - attach metadata per chunk: source filename, equipment type/model if
    you can parse it from the filename or header — the router/grader will
    want this later for filtering
  - the bundled manuals extract cleanly with plain text extraction, but a
    real scanned manual often won't: if PyPDFLoader returns empty text for
    a page, fall back to OCR on that page's rendered image (pytesseract +
    pdf2image, or PyPDF2's page.images the way
    github.com/jamwithai/beginner-local-rag-system/blob/main/src/ocr.py
    does it) rather than silently dropping the page

TODO (incidents):
  - load data/incidents/*.csv into a pandas DataFrame or a local SQLite
    table — pick whichever you want to practice querying against
    (df.query / pandasql vs real SQL)
"""
