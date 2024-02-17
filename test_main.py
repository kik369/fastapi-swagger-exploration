from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_item():
    item_data = {"name": "example", "price": 10.99}
    expected_response = {
        "name": "example",
        "price": 10.99,
        "description": None,
        "tax": None,
    }
    response = client.post("/items2/", json=item_data)
    assert response.status_code == 200
    assert response.json() == expected_response
