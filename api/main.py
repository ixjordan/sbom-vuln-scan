from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Vulnerability Scanner API")

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return{"message": "SBOM scanner API is running..."}