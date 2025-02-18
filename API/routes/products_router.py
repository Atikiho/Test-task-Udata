import json

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

routes = APIRouter()


@routes.get("/all_products/")
def get_all_products():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise HTTPException(status_code=500, detail="Data file is missing or invalid")
    return JSONResponse(content=data)


@routes.get("/products/{product_name}")
def get_product_by_name(product_name: str):
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise HTTPException(status_code=500, detail="Data file is missing or invalid")
    products = [product for product in data if product_name in product.get("name")]
    return JSONResponse(content=products)


@routes.get("/products/{product_name}/{product_field}")
def get_product_field(product_name: str, product_field: str):
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise HTTPException(status_code=500, detail="Data file is missing or invalid")
    products = [product.get(product_field) for product in data if product_name in product.get("name")]
    return JSONResponse(content=products)
