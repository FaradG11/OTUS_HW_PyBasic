from fastapi import APIRouter

from .db_queries import new_income, query_all_product
from .schemas import ProductIn, ProductOut


router = APIRouter(prefix="/products", tags=['products'])


@router.post("", response_model=ProductOut)
def add_some_product(product_in: ProductIn):
    return new_income(product_in)


@router.get("", response_model_include={"id", "pname", "amount"})
def list_of_product():
    return query_all_product()

