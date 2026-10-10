from fastapi.testclient import TestClient
from app.main import app
CASES=[("remote days","kb-1"),("expense receipt","kb-2"),("security incident","kb-3")]
def test_retrieval_regression():
    client=TestClient(app)
    for question,source in CASES:
        r=client.post("/knowledge/ask",json={"question":question})
        assert r.status_code==200
        assert r.json()["citations"][0]["source_id"]==source
