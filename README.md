## Basic online Store API (for learning purpose) :tm:

### API Endpoints:
This project provides a RESTful API for managing user data. The following endpoints are available:
> [!NOTE]
> Base endpoint __localhost:8000/api/v1/...__ ,all data is sent/received in JSON format 

1. [Customer](/customer/README.md) :white_check_mark:
   - [ ] **POST** /customer
   - [ ] **GET** /customer
   - [ ] **GET** /list-customers
   - [ ] **DELETE** /delete-customer
   - [ ] **PATCH** /change-email
   - [ ] **PATCH** /change-password
   - [ ] **PATCH** /update-customer

2. [Category](/category/README.md) :x:
   - [ ] **GET** /list_categories
   - [ ] **POST** /category
   - [ ] **GET** /category
   - [ ] **PATCH** /update_category
   - [ ] **DELETE** /delete_category

3. [Product](/product/README.md) :x:
   - [ ] **GET** /list_products
   - [ ] **GET** /products
   - [ ] **POST** /products
   - [ ] **PATCH** /update_product
   - [ ] **DELETE** /delete_product

4. [Orders](/orders/README.md) :x:
   - [ ] **GET** /list_orders
   - [ ] **GET** /order
   - [ ] **POST** /order
   - [ ] **PATCH** /update_order
   - [ ] **DELETE** /delete_order



### DB Key Relationship
- Customer -> Order: `customer.id (PK)` :arrow_left: `order.customer_id (FK)`
- Category -> Product: `category.id (PK)` :arrow_left: `product.category_id (FK)`
- Product -> Order: `product.id (PK)` :arrow_left: `order.items`

Check scripts folder to start SurrealDB server. You should have surrealDB installed locally.


## TODO :soon:
- add logging
- add tests
- add CI/CD