from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_document_list():
    response=client.get("/knowledge/documents")
    assert response.status_code==200
    assert len(response.json()["documents"])==3
    assert response.json()["documents"][0]["id"]=="kb-1"
