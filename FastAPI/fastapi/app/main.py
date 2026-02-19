from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Set, Tuple
from DataFetch.data import get_allproducts

app = FastAPI(
    title="First my api app", description="this my first app", version="1.0.0"
)


# root folder structure
@app.get("/")
def home_page():
    return "This is home page"


home_page()


# @app.get("/products")
# def print_all():
#     return get_allproducts()


@app.get("/products")
def list_products(
    name: str = Query(
        default=None, min_length=1, max_length=100, description="searh product by name"
    )
):
    return name


# products = ["apple", "banana", "pine"]


# @app.get("/products/{id}")
# def get_products(id: int):
#     try:
#         for each_product in products:
#             if products[id] == each_product[id]:
#                 return each_product
#     except Exception as e:
#         return f"{e}"
