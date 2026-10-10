from fastapi import FastAPI
from app.features.knowledge.door import router
app=FastAPI(title="Northstar Knowledge Assistant")
app.include_router(router)
