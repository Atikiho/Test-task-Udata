import json

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

routes = APIRouter()


def read_products_file():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise HTTPException(status_code=500, detail="Data file is missing or invalid")
    return data


@routes.get("/all_products/")
def get_all_products():
    data = read_products_file()
    return JSONResponse(content=data)


@routes.get("/products/{product_name}")
def get_product_by_name(product_name: str):
    data = read_products_file()
    products = [
        product
        for product in data
        if product_name.lower() in product.get("name").lower()
    ]
    if not products:
        raise HTTPException(
            status_code=404,
            detail=f"No products found with name containing '{product_name}'"
        )
    return JSONResponse(content=products)


@routes.get("/products/{product_name}/{product_field}")
def get_product_field(product_name: str, product_field: str):
    data = read_products_file()
    products = [
        product.get(product_field)
        for product in data
        if product_name.lower() in product.get("name").lower()
    ]
    if not any(products):
        raise HTTPException(
            status_code=404,
            detail=f"No products found with name containing '{product_name}' or field '{product_field}'",
        )
    return JSONResponse(content=products)
