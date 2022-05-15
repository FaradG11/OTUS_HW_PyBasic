from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as SessionType

from .db_queries import new_income, query_all_product, get_db
from .schemas import ProductIn, ProductOut, Product


router = APIRouter(prefix="/products", tags=['products'])


@router.post("", response_model=ProductOut)
def add_some_product(product_in: ProductIn, db: SessionType = Depends(get_db)):
    return new_income(db, product_in)


@router.get("", response_model=list[Product])
def list_of_product(db: SessionType = Depends(get_db)):
    return query_all_product(db)

