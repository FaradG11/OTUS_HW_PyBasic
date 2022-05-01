from pydantic import BaseModel, constr, Field


class ProductBase(BaseModel):
    name: constr(min_length=2)


class ProductIn(ProductBase):
    amount: int


class ProductOut(ProductBase):
    id: int


class Product(ProductOut):
    pass
