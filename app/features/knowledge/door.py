from fastapi import APIRouter
from app.features.knowledge.handlers import handle_documents
router=APIRouter(prefix="/knowledge", tags=["Knowledge"])
@router.get("/documents")
def documents()->dict:
    return handle_documents()
