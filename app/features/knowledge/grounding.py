# Verify the selected source and exact chunk; do not let answer text invent evidence.
from app.features.knowledge.chunking import service_chunk_documents
from app.features.knowledge.services import service_list_documents
def service_verify_citations(result:dict)->dict:
    if result["status"]!="grounded": return result
    chunks={x["id"]:x for x in service_chunk_documents(service_list_documents())}
    valid=any(c["chunk_id"] in chunks and chunks[c["chunk_id"]]["source_id"]==c["source_id"] and chunks[c["chunk_id"]]["text"]==result["answer"] for c in result["citations"])
    if not valid: return {"answer":None,"citations":[],"status":"insufficient_evidence"}
    return result
