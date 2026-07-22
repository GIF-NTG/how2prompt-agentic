import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client() -> TestClient:
    """
    Returns a FastAPI TestClient configured for testing.
    """
    return TestClient(app)
