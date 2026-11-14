from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_has_welcome_and_useful_links() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the DevOps Journey API",
        "docs": "/docs",
        "health": "/health",
    }


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_items() -> None:
    response = client.get("/api/v1/items")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "sample-item"


def test_get_existing_item() -> None:
    response = client.get("/api/v1/items/2")

    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "devops",
        "description": "Ready for the DevOps journey.",
    }


def test_get_missing_item_returns_404() -> None:
    response = client.get("/api/v1/items/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
