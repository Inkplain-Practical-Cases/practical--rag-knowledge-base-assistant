from app.features.knowledge.services import service_list_documents
def handle_documents()->dict:
    return {"documents":service_list_documents()}
