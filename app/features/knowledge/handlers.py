from app.features.knowledge.services import service_list_documents
from app.features.knowledge.chunking import service_chunk_documents
from app.features.knowledge.retrieval import service_rank_evidence
from app.features.knowledge.answers import service_compose_answer
def handle_documents()->dict: return {"documents":service_list_documents()}
def handle_chunks()->dict: return {"chunks":service_chunk_documents(service_list_documents())}
def handle_search(question:str)->dict: return {"evidence":service_rank_evidence(question)}
def handle_ask(question:str)->dict: return service_compose_answer(question)
