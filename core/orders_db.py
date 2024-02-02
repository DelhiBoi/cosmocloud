from conf.mongo import order_collection


def create_order(order_dict):
    order_collection.insert_one(order_dict)
    return True
