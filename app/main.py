from fastapi import FastAPI
from app.features.knowledge.door import router
app=FastAPI(title="Northstar Knowledge Assistant")
app.include_router(router)

# Persist metadata-only knowledge API outcomes without adding fake vector stores.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
