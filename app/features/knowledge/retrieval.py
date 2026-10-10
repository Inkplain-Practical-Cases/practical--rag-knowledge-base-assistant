import re
from app.features.knowledge.chunking import service_chunk_documents
from app.features.knowledge.services import service_list_documents
def service_rank_evidence(query:str,limit:int=3)->list[dict]:
    # Lexical retrieval is deterministic: no external embeddings service.
    tokens=set(re.findall(r"[a-z0-9]+",query.lower()))
    if not tokens: return []
    scored=[]
    for item in service_chunk_documents(service_list_documents()):
        words=set(re.findall(r"[a-z0-9]+",item["text"].lower()))
        score=len(tokens.intersection(words))
        if score: scored.append({**item,"score":score})
    return sorted(scored,key=lambda x:(-x["score"],x["id"]))[:limit]
