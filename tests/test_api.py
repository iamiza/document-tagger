from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_pdf():
    with open("sample.pdf", "rb") as f:
        response = client.post("/upload", files={"file": ("sample.pdf", f, "application/pdf")})
    assert response.status_code == 200
    assert "tags" in response.json()
