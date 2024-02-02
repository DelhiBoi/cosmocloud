from conf.mongo import collection


def get_products_list(json_query):
    results = collection.find(json_query)
    return list(results)


def bulk_update_products(updates):
    collection.bulk_write(updates)
