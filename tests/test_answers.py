from fastapi.testclient import TestClient
from app.main import app
def test_answer_is_cited():
    r=TestClient(app).post("/knowledge/ask",json={"question":"security incident report"})
    assert r.status_code==200
    j=r.json()
    assert j["status"]=="grounded"
    assert j["citations"][0]["source_id"]=="kb-3"
    assert "incident" in j["answer"].lower()
