# SQL Library FastAPI

A Library REST API built with **Python, FastAPI, PostgreSQL, and SQLAlchemy**.

This project demonstrates how to connect a FastAPI application to a real relational database and perform CRUD (Create, Read, Update, Delete) operations using SQLAlchemy ORM.

All book records are stored in PostgreSQL, ensuring that data persists even after the application is restarted.

## Features

- Retrieve all books
- Retrieve a specific book by ID
- Add a new book
- Update an existing book
- Delete a book
- Automatic ID generation by PostgreSQL
- Data validation using Pydantic
- Persistent data storage with PostgreSQL

## Technologies

- **Python** – Programming language
- **FastAPI** – Web framework for building APIs
- **Uvicorn** – ASGI server
- **uv** – Python package and project manager
- **PostgreSQL** – Relational database
- **SQLAlchemy** – ORM for database operations
- **Pydantic** – Data validation and serialization

## Book Data Model

Each book contains the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique book ID (auto-generated) |
| `title` | String | Book title |
| `author` | String | Book author |
| `year` | Integer | Publication year |

Example JSON:

```json
{
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937
}
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Retrieve all books |
| GET | `/books/{book_id}` | Retrieve a book by ID |
| POST | `/books` | Add a new book |
| PUT | `/books/{book_id}` | Update an existing book |
| DELETE | `/books/{book_id}` | Delete a book |

### 1. Get All Books

```http
GET /books
```

Returns a list of all books stored in the database.

### 2. Get a Specific Book

```http
GET /books/1
```

Returns the book with ID `1`.

### 3. Add a New Book

```http
POST /books
```

Example request body:

```json
{
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year": 1954
}
```

The database automatically generates a unique ID for the new book.

### 4. Update a Book

```http
PUT /books/1
```

Example request body:

```json
{
    "title": "The Hobbit Updated",
    "author": "J.R.R. Tolkien",
    "year": 1937
}
```

Updates the information of the book with ID `1`.

### 5. Delete a Book

```http
DELETE /books/3
```

Deletes the book with ID `3` from the database.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.15
- PostgreSQL
- pgAdmin (optional, for database management)
- uv

### 1. Clone the Repository

```bash
git clone <repository-url>
cd sql-library-fastapi
```

### 2. Create the Database

Open pgAdmin and create a new PostgreSQL database named:

```text
books_db
```

### 3. Configure Database Connection

Open:

```text
src/sql_library_fastapi/database.py
```

Make sure the PostgreSQL connection settings match your local configuration, including:

- Username
- Password
- Host
- Port
- Database name

### 4. Run the Application

Start the development server using:

```bash
python3.15 -m uv run uvicorn src.sql_library_fastapi.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI.

Once the server is running, open:

**Swagger UI:**

http://127.0.0.1:8000/docs

**ReDoc:**

http://127.0.0.1:8000/redoc

You can use these interfaces to test all available endpoints, including GET, POST, PUT, and DELETE requests.

## Data Persistence

This project uses PostgreSQL as its database instead of storing data in Python lists or temporary variables.

All changes are saved directly to the database. Therefore, adding, updating, or deleting books will not be lost when the application restarts.

## Project Goals

The main purpose of this project is to gain practical experience with:

- Connecting FastAPI to PostgreSQL
- Working with SQLAlchemy ORM
- Performing CRUD operations
- Validating request data with Pydantic
- Managing database connections
- Structuring a Python project using `uv`
- Building RESTful APIs with FastAPI

---

**Project:** SQL Library FastAPI  
**Status:** Learning Project  
**Language:** Python
