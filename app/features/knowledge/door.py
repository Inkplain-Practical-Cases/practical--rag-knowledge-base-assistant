from fastapi import APIRouter
from app.features.knowledge.handlers import handle_documents,handle_chunks
router=APIRouter(prefix="/knowledge", tags=["Knowledge"])
@router.get("/documents")
def documents()->dict: return handle_documents()
@router.get("/chunks")
def chunks()->dict: return handle_chunks()
