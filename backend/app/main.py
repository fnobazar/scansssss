from fastapi import FastAPI

app = FastAPI(
    title="Sca-N API",
    description="Scan, Understand, Research, Ask, Save",
    version="0.1.0",
)


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
