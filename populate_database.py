from constants.database_constants import DatabaseConstants
from conf.mongo import db
import json

with open('products.json', 'r') as file:
    data = json.load(file)

print(data)
collection = db[DatabaseConstants.PRODUCTS_COLLECTION]

result = collection.insert_many(data)
