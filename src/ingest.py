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

TODO (incidents):
  - load data/incidents/*.csv into a pandas DataFrame or a local SQLite
    table — pick whichever you want to practice querying against
    (df.query / pandasql vs real SQL)
"""
