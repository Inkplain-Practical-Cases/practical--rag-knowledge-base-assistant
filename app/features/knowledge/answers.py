from app.features.knowledge.retrieval import service_rank_evidence
from app.features.knowledge.grounding import service_verify_citations
def service_compose_answer(question:str)->dict:
    hits=service_rank_evidence(question,3)
    if not hits: return {"answer":None,"citations":[],"status":"insufficient_evidence"}
    best=hits[0]
    draft={"answer":best["text"],"citations":[{"source_id":best["source_id"],"chunk_id":best["id"]}],"status":"grounded"}
    return service_verify_citations(draft)
