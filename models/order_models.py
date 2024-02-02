from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    productId: str
    boughtQuantity: int


class Address(BaseModel):
    city: str
    country: str
    zipcode: str


class Order(BaseModel):
    items: List[Product]
    amount: float
    address: Address
