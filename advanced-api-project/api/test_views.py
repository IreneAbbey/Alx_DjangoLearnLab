from django.urls import reverse
from django.contrib.auth.models import User  # Import User model for authentication
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Author, Book
from api.serializers import BookSerializer


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")  # Login for authentication

    def test_create_book(self):
        url = reverse('book-list')
        author = Author.objects.create(name="William S. Vincent")  # Fix: Author should be an instance
        data = {"title": "Django for Beginners", "author": author.id, "publication_year": 2021}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Django for Beginners")

    def test_get_books(self):
        author = Author.objects.create(name="Eric Matthes")
        Book.objects.create(title="Python Crash Course", author=author, publication_year=2019)

        url = reverse('book-list')
        response = self.client.get(url)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_book(self):
        author = Author.objects.create(name="Eric Matthes")
        book = Book.objects.create(title="Python Crash Course", author=author, publication_year=2019)

        url = reverse('book-detail', kwargs={'pk': book.pk})  # Fix: Ensure correct view name
        new_author = Author.objects.create(name="New Author")  # Fix: Assign an actual Author instance
        data = {"title": "New Title", "author": new_author.id, "publication_year": 2022}
        response = self.client.put(url, data, format='json')

        book.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(book.title, "New Title")

    def test_delete_book(self):
        author = Author.objects.create(name="Unknown")  # Fix: Assign an Author instance
        book = Book.objects.create(title="To Be Deleted", author=author, publication_year=2023)

        url = reverse('book-detail', kwargs={'pk': book.pk})  
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_search_books(self):
        author1 = Author.objects.create(name="Jane Doe")
        author2 = Author.objects.create(name="John Doe")

        Book.objects.create(title="Django Guide", author=author1, publication_year=2021)
        Book.objects.create(title="Python Basics", author=author2, publication_year=2022)

        url = reverse('book-list') + "?search=Django"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Django Guide")
