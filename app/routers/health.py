from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])

class HealthResponse(BaseModel):
    status: str
    service: str

@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Standard health check endpoint.
    """
    return HealthResponse(status="healthy", service="how2prompt-agentic")
