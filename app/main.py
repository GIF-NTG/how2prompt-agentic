from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import agent, health
from app.core.logging import setup_logging

# Initialize Logging
setup_logging()

app = FastAPI(
    title="how2prompt-agentic",
    description="Stateless agentic service for optimizing and assembling prompts",
    version="1.0.0",
)

# Exception handlers for RFC-7807 responses
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Catch-all exception handler to return error details formatted as RFC-7807 problem details.
    """
    return JSONResponse(
        status_code=500,
        content={
            "type": "https://how2prompt.com/errors/internal-server-error",
            "title": "Internal Server Error",
            "status": 500,
            "detail": str(exc),
            "instance": request.url.path,
            "error_code": "INTERNAL_SERVER_ERROR",
        },
    )

# Include Routers
app.include_router(agent.router, prefix="/api/v1")
app.include_router(health.router)
