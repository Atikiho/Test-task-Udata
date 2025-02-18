import json
from typing import List

from fastapi import HTTPException


def read_products_file() -> List[dict]:
    try:
        with open("API/products.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise HTTPException(status_code=500, detail=f"Data file is missing or invalid")
    return data
