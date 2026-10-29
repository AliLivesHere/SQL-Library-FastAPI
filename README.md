SQL Library FastAPI

This is a Library API built with Python, FastAPI, and PostgreSQL.
The project is made for learning how to connect APIs to a real database and perform CRUD operations.
The book data is stored in a PostgreSQL database using SQLAlchemy, so all data is saved permanently.
Features

The API can:

    Get all books

    Get a specific book by ID

    Add a new book

    Update a book

    Delete a book

Technologies

    Python

    FastAPI

    Uvicorn

    uv

    PostgreSQL

    SQLAlchemy

    Pydantic

Book Data

Each book contains the following information:
JSON

{
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937
}

API Endpoints
Get All Books

GET /books

Returns all books in the library.
Get a Specific Book

GET /books/{book_id}

Example:GET /books/1

Returns the book with ID 1.
Add a New Book

POST /books

Example request:
JSON

{
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year": 1954
}

The book ID is created automatically by the database.
Update a Book

PUT /books/{book_id}

Example:PUT /books/1

Example request:
JSON

{
    "title": "The Hobbit Updated",
    "author": "J.R.R. Tolkien",
    "year": 1937
}

Delete a Book

DELETE /books/{book_id}

Example:DELETE /books/3

Deletes the book with ID 3.
Running the Project

1. Database Setup:
Create a new database named books_db in pgAdmin (PostgreSQL). Ensure the username, password, and port in src/sql_library_fastapi/database.py match your local PostgreSQL credentials.

2. Start the Server:
Run the following command:
Bash

python3.15 -m uv run uvicorn src.sql_library_fastapi.main:app --reload

The API will be available at:http://127.0.0.1:8000
API Documentation

FastAPI automatically provides API documentation using Swagger UI.
You can open it here:http://127.0.0.1:8000/docs

From this page, you can test the GET, POST, PUT, and DELETE requests.
Note

The current version uses a real PostgreSQL database. The books are stored permanently.
This means that changes made to the books will not be lost when the application is restarted.
Project Goal

The main goal of this project is to learn how to:

    Connect FastAPI to a PostgreSQL database

    Use SQLAlchemy ORM to manage tables and queries

    Validate incoming data with Pydantic

    Structure a Python project properly using uv
