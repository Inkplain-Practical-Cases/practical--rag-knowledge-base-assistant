from fastapi.testclient import TestClient
from app.main import app
def test_retrieval_is_ranked_and_cited():
    r=TestClient(app).post("/knowledge/search",json={"question":"manager approval expense claim"})
    assert r.status_code==200
    assert r.json()["evidence"][0]["source_id"]=="kb-2"
def test_empty_question_is_invalid():
    assert TestClient(app).post("/knowledge/search",json={"question":"x"}).status_code==422
