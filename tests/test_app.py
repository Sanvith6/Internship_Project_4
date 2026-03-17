import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_ok(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, World!"
    assert data["status"] == "ok"


def test_health_returns_healthy(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_unknown_route_returns_404(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
