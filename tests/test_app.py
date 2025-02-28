from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_shorten_url():
    response = client.post("/shorten", json={"long_url": "https://example-of-long-url.com"})
    assert response.status_code == 200
    assert "short_url" in response.json()

def test_redirect_url():
    response = client.get("/abc123")
    assert response.status_code in [200, 404]
