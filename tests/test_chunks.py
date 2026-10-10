from fastapi.testclient import TestClient
from app.main import app
def test_chunks_preserve_sources():
    r=TestClient(app).get("/knowledge/chunks")
    assert r.status_code==200
    assert all(x["source_id"] in {"kb-1","kb-2","kb-3"} for x in r.json()["chunks"])
