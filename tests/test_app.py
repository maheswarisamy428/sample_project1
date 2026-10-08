"""Tests for the DevSecOps AI Service."""

from fastapi.testclient import TestClient  # type: ignore[import-not-found]

from app.main import app

client = TestClient(app)


def test_health():
    """Test that the health endpoint returns a healthy status."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"