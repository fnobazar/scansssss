from fastapi import FastAPI

from app.api.agent import router as agent_router
from app.api.scan import router as scan_router
from app.api.search import router as search_router
from app.api.ask import router as ask_router
from app.api.discoveries import router as discoveries_router
from app.api.saved import router as saved_router

from app.config.cors import configure_cors


app = FastAPI(
    title="Sca-N API",
    description="Scan, Understand, Research, Ask, Save",
    version="0.1.0",
)

configure_cors(app)

app.include_router(agent_router, prefix="/v1")
app.include_router(scan_router, prefix="/v1")
app.include_router(search_router, prefix="/v1")
app.include_router(ask_router, prefix="/v1")
app.include_router(discoveries_router, prefix="/v1")
app.include_router(saved_router, prefix="/v1")


@app.get("/")
def root():
    return {
        "app": "Sca-N",
        "status": "running",
        "message": "Sca-N backend is ready",
    }


@app.get("/health")
def health():
    return {"status": "ok"}
