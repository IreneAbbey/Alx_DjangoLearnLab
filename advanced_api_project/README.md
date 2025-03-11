# Django REST Framework - Book API

## Overview
This API allows users to perform CRUD operations on books. It uses Django REST Framework's generic views and permissions.

## API Endpoints

| Method | Endpoint                | Description                   | Permissions |
|--------|-------------------------|-------------------------------|-------------|
| GET    | `/api/books/`           | List all books                | Public |
| GET    | `/api/books/<id>/`      | Retrieve a book by ID         | Public |
| POST   | `/api/books/create/`    | Create a new book             | Authenticated users |
| PUT    | `/api/books/<id>/update/` | Update an existing book    | Authenticated users |
| DELETE | `/api/books/<id>/delete/` | Delete a book               | Authenticated users |

## Permissions
- Unauthenticated users can **view** books.
- Authenticated users can **create, update, and delete** books.
- Admin users have full control.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
