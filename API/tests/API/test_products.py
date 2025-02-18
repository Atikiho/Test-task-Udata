import pytest
from fastapi.testclient import TestClient
from pydantic_core import ValidationError

from API.tests.conftest import mock_read_products_file, mock_return_value


def test_read_products(client: TestClient):
    response = client.get("/all_products/")
    assert response.status_code == 200
    assert response.json() == mock_read_products_file()


def test_read_existing_product(client: TestClient):
    response = client.get("/products/Чай зелений")
    assert response.status_code == 200

    expected_data = mock_read_products_file()
    assert response.json() == expected_data


def test_read_non_existing_product(client: TestClient):
    response = client.get("/products/Кока-Кола")
    assert response.status_code == 404
    assert response.json() == {
       'detail': "No products found with name containing 'Кока-Кола'",
    }


def test_read_existing_product_field(client: TestClient):
    response = client.get("/products/Чай зелений/portion")

    assert response.status_code == 200
    assert response.json() == [300]


def test_read_non_existing_product_field(client: TestClient):
    response = client.get("/products/Чай зелений/portions")

    assert response.status_code == 404
    assert response.json() == {
        'detail': "No products found with name containing 'Чай зелений' or field 'portions'",
    }


def test_invalid_data_full_list(client: TestClient):
    mock_return_value[0]["fats"] = -10
    with pytest.raises(ValidationError):
        client.get("/products/Чай зелений")
