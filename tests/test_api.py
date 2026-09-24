import pytest
from fastapi.testclient import TestClient
from main import app

def test_health_check():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["model_loaded"] == True

def test_classify_positive():
    with TestClient(app) as client:
        response = client.post("/v1/classify", json={"text": "Отличный продукт"})
        assert response.status_code == 200
        data = response.json()
        assert "label" in data
        assert data["label"] == "POSITIVE"

def test_classify_negative():
    with TestClient(app) as client:
        response = client.post("/v1/classify", json={"text": "Ужасное качество"})
        assert response.status_code == 200
        data = response.json()
        assert "label" in data
        assert data["label"] == "NEGATIVE"

def test_missing_field():
    with TestClient(app) as client:
        response = client.post("/v1/classify", json={})
        assert response.status_code == 422

def test_response_schema():
    with TestClient(app) as client:
        response = client.post("/v1/classify", json={"text": "test"})
        data = response.json()
        assert "label" in data
        assert "score" in data
        assert isinstance(data["score"], float)
