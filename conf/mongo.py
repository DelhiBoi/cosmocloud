from pymongo import MongoClient
from constants.database_constants import DatabaseConstants

mongo_uri = f"mongodb://localhost:27017"

client = MongoClient(mongo_uri)

db = client[DatabaseConstants.DATABASE_NAME]

collection = db[DatabaseConstants.PRODUCTS_COLLECTION]

order_collection = db[DatabaseConstants.ORDER_COLLECTION]
