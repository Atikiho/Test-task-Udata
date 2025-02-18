import json


def test_read_products(client):
    response = client.get("/all_products/")
    assert response.status_code == 200
    with open("products.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    assert response.json() == data
