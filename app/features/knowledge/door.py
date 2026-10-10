from fastapi import APIRouter
from pydantic import BaseModel,Field
from app.features.knowledge.handlers import handle_documents,handle_chunks,handle_search,handle_ask
router=APIRouter(prefix="/knowledge",tags=["Knowledge"])
class Query(BaseModel):
    question:str=Field(min_length=3,max_length=300)
@router.get("/documents")
def documents()->dict: return handle_documents()
@router.get("/chunks")
def chunks()->dict: return handle_chunks()
@router.post("/search")
def search(body:Query)->dict: return handle_search(body.question)
@router.post("/ask")
def ask(body:Query)->dict: return handle_ask(body.question)
