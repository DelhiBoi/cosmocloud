from fastapi import APIRouter
from handlers.order_handler import place_order
from models.order_models import Order

router = APIRouter()


@router.post("/order/")
def read_items(order: Order):
    return place_order(order_dict=order.dict())
