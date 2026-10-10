from app.features.knowledge.services import service_list_documents
from app.features.knowledge.chunking import service_chunk_documents
from app.features.knowledge.retrieval import service_rank_evidence
def handle_documents()->dict: return {"documents":service_list_documents()}
def handle_chunks()->dict: return {"chunks":service_chunk_documents(service_list_documents())}
def handle_search(question:str)->dict: return {"evidence":service_rank_evidence(question)}
