from core.orders_db import create_order
from core.products_db import get_products_list, bulk_update_products
from datetime import datetime
from pymongo import UpdateOne
from bson import ObjectId


def place_order(order_dict: dict):
    # update created_on in order creation dict
    created_on = datetime.now()
    order_dict.update({"createdOn": created_on})

    # Data processing
    items = order_dict['items']
    requested_product_list = [ObjectId(item['productId']) for item in items]
    query = {"_id": {"$in": requested_product_list}}
    product_list = get_products_list(json_query=query)
    product_quantity_map = {}
    for product in product_list:
        product_quantity_map[product["_id"]] = product["quantity"]

    product_price_map = {}
    for product in product_list:
        product_price_map[product["_id"]] = product["price"]

    # Validate if all the requested products are even available in catalogue
    are_products_valid = validate_product_ids(
        requested_product_list, product_list)
    if not are_products_valid:
        return "Order Cannot be created since at least one of the products not found"

    # Validate if we have sufficient quantity to place the order
    is_quantity_valid = validate_quantity(items, product_quantity_map)
    if not is_quantity_valid:
        return "Order cannot be placed due to quantity mismatch"

    # Validate whether sufficient amount of money was sent or not
    total_order_amount = 0
    for item in items:
        total_order_amount = total_order_amount + \
            product_price_map[ObjectId(item["productId"])]
    if total_order_amount > order_dict["amount"]:
        return "Order cannot be placed because insufficient amount"

    # Create order
    create_order(order_dict)

    # Update inventory
    update_operations = [
        UpdateOne({"_id": product["_id"]}, {
                  "$set": {"quantity": product_quantity_map[product["_id"]]}})
        for product in product_list
    ]
    bulk_update_products(update_operations)

    return "Order Created Successfully"


def validate_product_ids(requested_product_list, product_list):
    if len(product_list) != len(requested_product_list):
        return False

    return True


def validate_quantity(items, product_quantity_map):
    for item in items:
        product_id = ObjectId(item['productId'])
        quantity_requested = item['boughtQuantity']

        if quantity_requested > product_quantity_map[product_id]:
            return False

        product_quantity_map[product_id] = product_quantity_map[product_id] - \
            quantity_requested

    return True
