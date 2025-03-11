from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Author, Book
from api.serializers import BookSerializer


class BookAPITestCase(APITestCase):
    def test_create_book(self):
        url = reverse('book-list')
        data = {"title": "Django for Beginners", "author": "William S. Vincent", "publication_year": 2021}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Django for Beginners")

    def test_get_books(self):
        Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2019)

        url = reverse('book-list')
        response = self.client.get(url)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_book(self):
        author = Author.objects.create(name="Eric Matthes")  # Replace with actual fields
        Book.objects.create(title="Python Crash Course", author=author, publication_year=2019)

        url = reverse('book-detail', kwargs={'pk': Book.pk})  # Update with your view name
        data = {"title": "New Title", "author": "New Author", "publication_year": 2022}
        response = self.client.put(url, data, format='json')

        Book.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.title, "New Title")

    def test_delete_book(self):
        book = Book.objects.create(title="To Be Deleted", author="Unknown", publication_year=2023)

        url = reverse('book-detail', kwargs={'pk': book.pk})  # Update with your view name
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_search_books(self):
        Book.objects.create(title="Django Guide", author="Jane Doe", publication_year=2021)
        Book.objects.create(title="Python Basics", author="John Doe", publication_year=2022)

        url = reverse('book-list') + "?search=Django"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Django Guide")
