from typing import List

from fastapi import APIRouter, HTTPException, Depends

from schemas.products import ProductResponseSchema
from utils import read_products_file

routes = APIRouter()


@routes.get("/all_products/")
def get_all_products(data: List[dict] = Depends(read_products_file)):
    products = [ProductResponseSchema(**product) for product in data]
    return products


@routes.get("/products/{product_name}")
def get_product_by_name(
        product_name: str,
        data: List[dict] = Depends(read_products_file)
):
    products = [
        ProductResponseSchema(**product)
        for product in data
        if product_name.lower() in product.get("name").lower()
    ]
    if not products:
        raise HTTPException(
            status_code=404,
            detail=f"No products found with name containing '{product_name}'"
        )
    return products


@routes.get("/products/{product_name}/{product_field}")
def get_product_field(
        product_name: str,
        product_field: str,
        data: List[dict] = Depends(read_products_file)
):
    products = [
        product.get(product_field)
        for product in data
        if product_name.lower() in product.get("name").lower()
    ]
    if None in products:
        raise HTTPException(
            status_code=404,
            detail=f"No products found with name containing '{product_name}' or field '{product_field}'",
        )
    return products
