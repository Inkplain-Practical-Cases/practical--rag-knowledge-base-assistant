"""Check knowledge assistant audit request/event foreign keys."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit
def test_knowledge_audit_fk(tmp_path):
    db=str(tmp_path/"knowledge.sqlite3")
    rid=provider_record_request_audit("POST","/query",200,9.2,db)
    with sqlite3.connect(db) as con:
        assert con.execute("SELECT COUNT(*) FROM knowledge_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert con.execute("SELECT COUNT(*) FROM knowledge_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert con.execute("PRAGMA foreign_key_check").fetchall()==[]
