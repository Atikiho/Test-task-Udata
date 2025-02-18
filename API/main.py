from fastapi import FastAPI

from API.routes.products_router import routes as product_routes

app = FastAPI(title="Test-task-Udata")

app.include_router(product_routes)
