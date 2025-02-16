LibraryProject - Django Development Environment Setup
Introduction
This project is a basic Django setup for the LibraryProject, which will be used for learning Django development. The setup includes installing Django, creating a project, running a development server, and understanding the project structure.

Getting Started
Prerequisites
Ensure you have the following installed:

Python (3.x) → Check with python --version
pip (Python package manager)
Step 1: Install Django
Run the following command to install Django:

bash
Copy
Edit
pip install django
Verify installation:

bash
Copy
Edit
django-admin --version
Step 2: Create a Django Project
Run:

bash
Copy
Edit
django-admin startproject LibraryProject
This will create a folder named LibraryProject.

Step 3: Run the Development Server
Navigate into the project directory:

bash
Copy
Edit
cd LibraryProject
Run the server:

bash
Copy
Edit
python manage.py runserver
Now, open http://127.0.0.1:8000/ in your browser to see the Django welcome page.