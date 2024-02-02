from core.products_db import get_products_list


def product_list(filters):
    json_query = {}

    offset = filters.get("offset")
    limit = filters.get("limit")

    max_price = None
    if filters.get("max_price"):
        max_price = filters.get("max_price")

    min_price = 0
    if filters.get("min_price"):
        min_price = filters.get("min_price")

    if max_price or min_price:
        json_query = {
            "price": {"$gte": min_price, "$lte": max_price}
        }

    data = {"data": [], "page": {}}

    results = get_products_list(json_query)

    for product in results:
        data["data"].append({
            "name": product["name"],
            "quantity": product["quantity"],
            "price": product["price"],
        })
    data["data"] = data["data"][offset: offset + limit]

    data["page"]["total"] = len(data['data'])
    data["page"]["prevOffset"] = filters.get("offset")
    data["page"]["limit"] = filters.get("limit")
    data["page"]["nextOffset"] = filters.get("offset") + filters.get("limit")

    return data
