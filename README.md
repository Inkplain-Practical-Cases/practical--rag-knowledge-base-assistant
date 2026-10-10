# RAG Knowledge Base Assistant

Starter FDE practical case, six cumulative branches. Python 3.12, FastAPI, Pydantic, deterministic lexical ranking, exact evidence chunk citations and safe event logging.

```bash
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```

Endpoints GET /knowledge/documents, GET /knowledge/chunks, POST /knowledge/search and POST /knowledge/ask; use JSON {"question":"What is the remote work policy?"}. No API keys, paid LLM, private documents or model hallucination. Only synthetic corpus is indexed. Answers quote actual complete chunks and expose source_id/chunk_id. Unknown questions abstain.

Branches: step-01-receive-knowledge-documents, step-02-normalize-and-chunk-documents, step-03-rank-evidence-with-lexical-search, step-04-compose-grounded-answers, step-05-verify-citations-and-abstention, step-06-evaluate-and-monitor-retrieval. Every branch has STEP-N.crd, STEP-N.md, real code and tests; main FINAL.crd and Github Actions.

This is an educational extractive RAG-like assistant, **not** an actual LLM-driven generative RAG solution. Semantic embeddings, access-controlled documents and production data retention remain future work.
