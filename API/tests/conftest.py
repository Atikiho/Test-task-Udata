from typing import List

import pytest
from fastapi.testclient import TestClient

from API.main import app
from API.utils import read_products_file


@pytest.fixture(scope="function")
def client():
    app.dependency_overrides[read_products_file] = mock_read_products_file

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides[read_products_file] = None


def mock_read_products_file() -> List[dict]:
    return [
        {
            "name": "Чай зелений",
            "description": "Оригінальний зелений чай.",
            "calories": 0,
            "fats": 0,
            "carbs": 0,
            "protein": 0,
            "unsaturated_fats": 0,
            "sugar": 0,
            "salt": 0,
            "portion": 300
        }
    ]
