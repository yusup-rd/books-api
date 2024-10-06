# Book Inventory API

## Installation

1. Install Pipenv:
   ```bash
   pip isntall pipenv
2. Install dependencies from the Pipfile:
   ```bash
   pipenv isntall
3. Run the server:
   ```bash
   pipenv run python manage.py runserver

## Credentials

- **Admin**: `admin`, Password: `kxIKN8bm`
- **Author User**: `authoruser`, Password: `kxIKN8bm`
- **Basic User**: `basicuser`, Password: `kxIKN8bm`

## Content

This API allows authors to create, update, and delete book entries while providing read-only access to all users. Features include custom permissions, pagination, and filtering.

### Endpoints

| Method | Endpoint            | Description                          |
|--------|---------------------|--------------------------------------|
| GET    | `/api/books/`      | List all books                       |
| GET    | `/api/books/{id}/` | Get a specific book by ID           |
| POST   | `/api/books/`      | Create a new book                   |
| PUT    | `/api/books/{id}/` | Update an existing book             |
| DELETE | `/api/books/{id}/` | Delete a book                       |

