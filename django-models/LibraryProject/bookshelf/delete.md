# Delete a Book
from bookshelf.models import Book

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())