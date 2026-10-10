from app.features.knowledge.retrieval import service_rank_evidence
from app.features.knowledge.grounding import service_verify_citations
from app.core.observability import service_log_query_event
def service_compose_answer(question:str)->dict:
    hits=service_rank_evidence(question,3)
    if not hits: result={"answer":None,"citations":[],"status":"insufficient_evidence"}
    else:
        best=hits[0]
        draft={"answer":best["text"],"citations":[{"source_id":best["source_id"],"chunk_id":best["id"]}],"status":"grounded"}
        result=service_verify_citations(draft)
    service_log_query_event(result["status"],len(result["citations"]))
    return result
