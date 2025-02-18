from fastapi.testclient import TestClient
from API.tests.conftest import mock_read_products_file


def test_read_products(client: TestClient):
    response = client.get("/all_products/")
    assert response.status_code == 200

    expected_data = mock_read_products_file()
    assert response.json() == expected_data


def test_read_existing_product(client: TestClient):
    response = client.get("/products/Чай зелений")
    assert response.status_code == 200

    expected_data = mock_read_products_file()
    assert response.json() == expected_data


def test_read_non_existing_product(client: TestClient):
    response = client.get("/products/Кока-Кола")
    assert response.status_code == 404

    expected_data = {
       'detail': "No products found with name containing 'Кока-Кола'",
    }
    assert response.json() == expected_data


def test_read_existing_product_field(client: TestClient):
    response = client.get("/products/Чай зелений/portion")

    assert response.status_code == 200
    assert response.json() == [300]
