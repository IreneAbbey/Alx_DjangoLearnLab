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

# Security Enhancements in Django

## Overview
This project implements best practices for securing a Django application, protecting against XSS, CSRF, SQL injection, and Clickjacking.

## Security Measures

### **1. Secure Django Settings**
- `DEBUG = False` to prevent information leaks in production.
- **CSRF & Session Security**: Ensures secure cookie handling.
- **Clickjacking Protection**: `X_FRAME_OPTIONS = 'DENY'`
- **CSP Middleware**: Restricts allowed content sources.

### **2. CSRF Protection**
- All forms include `{% csrf_token %}` to prevent CSRF attacks.

### **3. Preventing SQL Injection**
- Use Django ORM with `.filter()` instead of raw SQL queries.
- Validate user input using Django forms.

### **4. CSP Implementation**
- Configured CSP headers to block unauthorized script execution.

## Testing Guide
- **Test CSRF Protection**: Try submitting forms without CSRF tokens.
- **Test SQL Injection**: Enter `" OR 1=1 --` in the search bar.
- **Test XSS**: Attempt `<script>alert('XSS')</script>` as input.

✅ **All security measures have been implemented successfully!**

# Security Measures Implemented
1. Enforced HTTPS redirects (SECURE_SSL_REDIRECT).
2. Configured HSTS to prevent MITM attacks.
3. Secured cookies to only transmit over HTTPS.
4. Implemented HTTP security headers (X-Frame-Options, XSS filter).
5. Deployed SSL certificates via Let's Encrypt.

# Potential Areas for Improvement
- Enable Content Security Policy (CSP) for additional XSS protection.
- Regularly rotate TLS certificates.


python manage.py migrate


