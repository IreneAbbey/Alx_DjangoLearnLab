# Create a Book

To create a book in Django using the ORM, run the following command in the Python shell:

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
Expected Output:
1984
