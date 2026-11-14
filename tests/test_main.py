from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_serves_learning_hub() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "mapped out." in response.text
    assert "/static/styles.css" in response.text
    assert response.text.count('class="module-card"') == 12


def test_learning_hub_javascript_is_served() -> None:
    response = client.get("/static/app.js")

    assert response.status_code == 200
    assert "javascript" in response.headers["content-type"]
    assert "filterCards" in response.text


def test_learning_hub_styles_are_served() -> None:
    response = client.get("/static/styles.css")

    assert response.status_code == 200
    assert "text/css" in response.headers["content-type"]


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
