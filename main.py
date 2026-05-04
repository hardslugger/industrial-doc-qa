"""
Industrial Document Q&A — Application Entry Point

A multilingual RAG system over industrial standards documents.
This is the v0 skeleton — only a /health endpoint for now.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Industrial Doc Q&A",
    description="Multilingual RAG over industrial standards documents",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    """Liveness probe — returns OK if the app is running."""
    return {"status": "ok"}