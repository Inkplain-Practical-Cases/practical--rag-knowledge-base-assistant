from app.providers.documents import provider_documents
def service_list_documents()->list[dict]:
    return provider_documents()
