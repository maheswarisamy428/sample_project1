"""FastAPI application for the DevSecOps AI Service."""

from fastapi import FastAPI  # type: ignore

app = FastAPI(title="DevSecOps AI Service")


@app.get("/health")
def health():
    """Return the health status of the service."""
    return {"status": "healthy"}


@app.get("/")
def home():
    """Return the service welcome message."""
    return {"message": "DevSecOps AI Service"}
