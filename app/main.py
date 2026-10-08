from fastapi import FastAPI  # type: ignore

app = FastAPI(title="DevSecOps AI Service")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/")
def home():
    return {"message": "DevSecOps AI Service"}
