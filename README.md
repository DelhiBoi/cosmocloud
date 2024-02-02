# CosmoCloud Backend Application

## Folder Structure:

- **conf:** For all database connection settings, pooling settings.
- **constants:** Holds constants.
- **controllers:** API Entry points (GET, POST, etc.).
- **core:** Database layer.
- **handlers:** Business Logic Layer.
- **models:** DTO's for communication between client and server.

**main.py:** Service entry point.

## Setup Instructions:

Assuming you have a mongo instance running on localhost at 27017

1. run build.sh bash script
2. Database should have been populated
3. Use ID's from database and populate the API's
4. Play around with API's using below curls

## API Documentation:

### 1. `/products/` - GET:

```bash

# Normal get call
curl -X 'GET' \
 'http://127.0.0.1:8000/products/?limit=10&offset=1' \
 -H 'accept: application/json'

# Get call with max and min price filters
curl --location --request GET 'http://127.0.0.1:8000/products/?limit=10&offset=1&max_price=80&min_price=20' \
--header 'accept: application/json'



### 2. `/order/` - POST:
curl --location --request POST 'http://127.0.0.1:8000/order/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "items": [
    {
      "productId": "<fill id>",
      "boughtQuantity": 2
    },
    {
      "productId": " <fill id> like :  65bca470623effb95563119e",
      "boughtQuantity": 3
    }
  ],
  "amount": 1500,
  "address": {
    "city": "Sample City",
    "country": "Sample Country",
    "zipcode": "12345"
  }
}'
```
