# Django Permissions and Groups Setup

## Overview
This project implements **role-based access control** using Django’s built-in permissions and groups.

## Permissions and Groups

### Permissions
The following custom permissions are defined for the `Book` model:
- `can_view` - Allows viewing books
- `can_create` - Allows adding books
- `can_edit` - Allows editing books
- `can_delete` - Allows deleting books

### Groups
- **Viewers**: Can only view books.
- **Editors**: Can create and edit books.
- **Admins**: Can create, edit, and delete books.

## Setup Instructions

### 1. Run Migrations
```bash
python manage.py migrate
