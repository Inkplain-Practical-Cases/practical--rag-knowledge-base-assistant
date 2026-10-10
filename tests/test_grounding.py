from fastapi.testclient import TestClient
from app.main import app
from app.features.knowledge.grounding import service_verify_citations
def test_fabricated_citation_is_rejected():
    bad={"answer":"Invented","citations":[{"source_id":"kb-1","chunk_id":"unknown"}],"status":"grounded"}
    assert service_verify_citations(bad)["status"]=="insufficient_evidence"
def test_no_hits_abstain():
    r=TestClient(app).post("/knowledge/ask",json={"question":"xylophone astronomy"})
    assert r.status_code==200
    assert r.json()["status"]=="insufficient_evidence"
