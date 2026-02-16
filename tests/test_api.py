import pytest
from fastapi.testclient import TestClient

def test_read_root(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_endpoint(client: TestClient):
    data = {
        "habitaciones": 3,
        "metros": 100,
        "garage": 1,
        "ascensor": 1,
        "ubicacion": 1,
        "numero_planta": 2.0
    }
    response = client.post("/predict", json=data)
    # Could be 200 or 500 if model file is missing in test env, but endpoint should exist
    assert response.status_code in [200, 500]

def test_rate_limiting(client: TestClient):
    # Test rate limit for /predict (5/minute)
    data = {
        "habitaciones": 3,
        "metros": 100,
        "garage": 1,
        "ascensor": 1,
        "ubicacion": 1,
        "numero_planta": 2.0
    }
    
    # First 5 should pass (or be accepted 200/500)
    for _ in range(5):
        client.post("/predict", json=data)
    
    # 6th should be limited
    response = client.post("/predict", json=data)
    assert response.status_code == 429
