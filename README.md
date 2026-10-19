# Industrial RAG Assistant

A learning project for sharpening LangChain/LangGraph skills by building an
agentic RAG system over real industrial maintenance data: OEM equipment
manuals (unstructured) and incident/RCA logs (structured).

This is deliberately **not** "upload a PDF, stuff a vector store, ask
questions." That pattern is table stakes and barely touches LangGraph. The
point of this project is to practice the parts of LangGraph that plain
vector RAG never exercises: routing, conditional edges, self-correction
loops, and mixed structured/unstructured retrieval.

## The scenario

You're building an assistant for technicians and supervisors at an
industrial valve/pump engineering firm (modeled on BRIMIS Engineering). It
should be able to answer questions like:

- "What's the recommended torque spec for tightening the gland packing on a
  [model] valve?" → **unstructured**, answered from an OEM manual
- "How many mechanical incidents involving pump seal failure did we log last
  quarter, and what were the root causes?" → **structured**, answered from
  the incident log
- "We just had a valve actuator failure — what did we do last time this
  happened, and does the manual recommend anything different?" → **both**,
  requires combining structured incident history with manual guidance

## Architecture (LangGraph state machine)

```
                 ┌─────────┐
                 │  route  │   classify: structured / semantic / both
                 └────┬────┘
            ┌─────────┼─────────┐
            ▼                   ▼
  ┌───────────────────┐  ┌──────────────────┐
  │ retrieve_structured│  │ retrieve_semantic│
  │ (query incident log)│  │ (vector search)  │
  └─────────┬──────────┘  └─────────┬────────┘
            └─────────┬─────────────┘
                       ▼
               ┌───────────────┐
               │grade_documents│──── weak? ──▶ loop back to retrieve
               └───────┬───────┘               (rephrase / re-route)
                       ▼
                 ┌──────────┐
                 │ generate │  answer with citations
                 └────┬─────┘
                      ▼
                 ┌──────────┐
                 │  verify  │  groundedness check before returning
                 └──────────┘
```

Nodes are stubbed in `src/graph/` with TODOs — the wiring and prompts are
intentionally left for you to implement as the learning exercise.

## Data

- `data/manuals/` — put a few real or representative OEM valve/pump manual
  PDFs here (check license/sharing terms if using real vendor docs; public
  spec sheets or your own BRIMIS user manual work fine too)
- `data/incidents/` — export a CSV from `BRIMIS_IMS.xlsx` (Incident Log
  sheet) as mock structured data, or synthesize one

Neither directory is populated in this scaffold — add your own data before
running anything.

## Roadmap / milestones

1. **Ingestion** — load + chunk manuals, embed into a vector store
   (`src/ingest.py`). Load incident CSV into a dataframe or SQLite table.
2. **Naive baseline** — wire a single retrieve → generate chain, just to
   confirm the data and embeddings work. Throw this away once step 3 works.
3. **Router node** — classify incoming questions by source type.
4. **Structured retrieval node** — natural-language-to-pandas/SQL query
   over the incident log.
5. **Semantic retrieval node** — vector search over manual chunks with
   metadata filtering (e.g. by equipment type).
6. **Grading + self-correction loop** — score retrieved context for
   relevance; on a low score, re-route or rephrase and retry (bounded, to
   avoid infinite loops).
7. **Generation with citations** — answers must cite the source document or
   incident ID they're grounded in.
8. **Verification node** — a cheap groundedness/hallucination check before
   returning the final answer.
9. **Eval** — a small fixed question set with expected source types/answers
   to catch regressions as you iterate (LangSmith or a plain pytest harness).

## Stack

- `langgraph` for the state machine
- `langchain` for loaders/splitters/retrievers
- A local vector store to start (Chroma or FAISS) — no need for a hosted
  vector DB for a learning project
- Any LLM provider you have API access to

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your API key(s)
```

## Non-goals (for now)

- No auth, no multi-user, no deployment — this is a local CLI/notebook
  project focused on the retrieval/reasoning graph, not productionization
- No fine-tuning — retrieval quality and graph design are the point
