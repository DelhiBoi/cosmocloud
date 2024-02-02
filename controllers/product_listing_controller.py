from fastapi import APIRouter
from typing import Union, Optional
from handlers.product_list_handler import product_list

router = APIRouter()


@router.get("/products/")
def read_items(limit: int, offset: int, max_price: Optional[int] = None, min_price: Optional[int] = None):
    query_parameters = {
        "limit": limit,
        "offset": offset,
        "max_price": max_price,
        "min_price": min_price
    }
    return product_list(filters=query_parameters)
