"""Health Check Endpoint"""
from fastapi import APIRouter
from app.schemas import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint
    
    Returns:
        HealthResponse with status
    """
    return {
        "status": "ok",
        "message": "AAI Backend is running"
    }
