## API description
- [x] **POST** /customer/ (Create a new customer.)
- [x] **GET** /customer/{id} (Retrieve a specific customer's details by email.)
- [x] **GET** /customer/ (Retrieve a list of customers.)
- [x] **DELETE** /customer/{id}/ (Delete a customer.)
- [ ] **PATCH** /update-customer/ (Update an existing customer's details.)
- [ ] **PATCH** /change-password/ (Update customer password.)
- [ ] **PATCH** /change-email/ (update the email address)

1. Create new customer.
```json
{
    "customer_type": "Regular",
    "name": "mistik",
    "email": "mistik@xmen.com",
    "password": "root",
    "age": 31,
    "phone": "+1-(343)-999-7812",
    "address": "1, xavier school"
}
```

2. Delete customer.
```json
{
  "email": "abc@xyz.com"
}
```

3. Retrieve a single customer.
```json
{
  "email": "abc@xyz.com"
}
```

4. Change password.
```json
{
    "email": "abc@xyz.com",
    "old_password": "root",
    "new_password": "root123"
}
```

5. Change email.
```json
{
    "email": "abc@xyz.com",
    "new_email": "mtn@xyz.com"
}
```

6. Update customer details, all fields except email are optional
```json
{
    "email": "abc@xyz.com",
    "customer_type": "Regular",
    "name": "Dru",
    "address": "1, Hacker way, Salisbury",
    "phone": "+1-(738)-2387-323"
}
