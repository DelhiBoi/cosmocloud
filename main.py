from fastapi import FastAPI
from controllers.product_listing_controller import router as product_router
from controllers.order_controller import router as order_router

app = FastAPI()

app.include_router(product_router)
app.include_router(order_router)
