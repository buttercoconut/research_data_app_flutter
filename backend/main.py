"""FastAPI application entry point for the Research Data App backend.

This module sets up the FastAPI instance, includes routers, and configures the database.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import research_data
from .database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Research Data API", description="API for managing research data records.")

# Allow CORS for mobile app (Flutter) running on localhost during dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(research_data.router, prefix="/api", tags=["research_data"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
