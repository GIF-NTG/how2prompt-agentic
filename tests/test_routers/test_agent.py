from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

def test_health_check(client: TestClient) -> None:
    """
    Verifies the health check endpoint returns 200 OK and valid JSON.
    """
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "how2prompt-agentic"

def test_optimize_endpoint_validation_error(client: TestClient) -> None:
    """
    Verifies that missing required payload fields trigger HTTP 422 validation errors.
    """
    # Send empty payload (missing prompt_idea)
    response = client.post("/api/v1/agent/optimize", json={})
    assert response.status_code == 422
