from fastapi import FastAPI
from routers import data

app = FastAPI(title="Research Data API")

app.include_router(data.router, prefix="/api/data", tags=["data"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Research Data API"}
