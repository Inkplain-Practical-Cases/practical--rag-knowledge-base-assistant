import json,logging
from app.core.observability import service_log_query_event
def test_safe_log(caplog):
    with caplog.at_level(logging.INFO,logger="rag.audit"): service_log_query_event("grounded",1)
    event=json.loads(caplog.records[-1].message)
    assert set(event)=={"event","status","citation_count"}
