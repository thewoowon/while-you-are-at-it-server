# 길 위에서 만나는 연결, 가는김에

![Pasted Graphic 23](https://github.com/user-attachments/assets/9b34deca-b99b-4e5c-8b1b-23f5446f98eb)
![Pasted Graphic 24](https://github.com/user-attachments/assets/504642d9-23eb-4617-9b6a-830e274849d9)
![Pasted Graphic 22123](https://github.com/user-attachments/assets/bdd729f5-3350-4302-8743-382e382a0754)
![Pasted Graphic 21123412](https://github.com/user-attachments/assets/e9bb0fb3-321c-4489-a05b-c048230a0ed5)

# API Documentation

## **1. POST /users/**

- **Description**: Create a new user
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```
- **Responses**:
  - **201 Created**:
    ```json
    {
      "message": "User created successfully",
      "user": {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30
      }
    }
    ```

## **2. GET /users/**

- **Description**: Retrieve a list of users
- **Query Parameters**:
  - `limit`: Number of users to return (default: 10)
- **Responses**:
  - **200 OK**:
    ```json
    {
      "message": "Returning 10 users"
    }
    ```
