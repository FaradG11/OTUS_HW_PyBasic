from pydantic import BaseModel, constr, Field


class ProductBase(BaseModel):
    name: str


class ProductIn(ProductBase):
    amount: int


class ProductOut(ProductIn):
    id: int


class Product(ProductOut):
    class Config:
        orm_mode = True
