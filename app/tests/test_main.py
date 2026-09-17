import pytest
from fastapi.testclient import TestClient

from app.main import app, releases

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_releases():
    releases.clear()  # Clear the releases list before each test
    yield
    releases.clear()  # Clear the releases list after each test

def sample_release():
    return {
        "version": "1.0.0",
        "environment": "dev",
        "status": "deployed",
        "commit_sha": "a82d910",
    }

def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0"}

def test_create_release():
    response = client.post(
        "/releases",
        json=sample_release()
    )

    assert response.status_code == 201
    data = response.json()
    assert data["version"] == "1.0.0"
    assert data["environment"] == "dev"
    assert data["status"] == "deployed"
    assert data["commit_sha"] == "a82d910"
    assert "id" in data
    assert "created_at" in data

def test_get_releases():
    client.post(
        "/releases",
        json=sample_release()
    )
    response = client.get("/releases")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["version"] == "1.0.0"

def test_get_release_by_id():
    create_response = client.post(
        "/releases",
        json=sample_release(),
    )

    release_id = create_response.json()["id"]
    response = client.get(f"/releases/{release_id}")
    assert response.status_code == 200
    assert response.json()["id"] == release_id
    assert response.json()["version"] == "1.0.0"

def test_get_unknown_release():
    unknown_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"/releases/{unknown_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Release not found"}

def test_reject_invalid_environment():
    invalid_release = sample_release()
    invalid_release["environment"] = "testing"
    response = client.post(
        "/releases",
        json=invalid_release,
    )
    assert response.status_code == 422

def test_reject_short_commit_sha():
    invalid_release = sample_release()
    invalid_release["commit_sha"] = "abc"
    response = client.post(
        "/releases",
        json=invalid_release,
    )