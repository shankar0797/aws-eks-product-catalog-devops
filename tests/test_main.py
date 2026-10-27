from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Product Catalog API",
        "status": "running",
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_list_products():
    response = client.get("/products")

    assert response.status_code == 200

    products = response.json()
    assert len(products) == 3
    assert products[0]["name"] == "Laptop"


def test_get_existing_product():
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Laptop",
        "price": 65000,
    }


def test_get_nonexistent_product():
    response = client.get("/products/999")

    assert response.status_code == 404


def test_version_endpoint():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}