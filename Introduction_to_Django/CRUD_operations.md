>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
1984 (most recent call last):
>>> book = Book.objects.get(title="1984")
itle, book.athor, book.publication_year)
>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
int(book.title)
>>> print(book.title)
Nineteen Eighty-Four
>>> book.delete()
return an empty queryset
(1, {'bookshelf.Book': 1})
>>> print(Book.objects.all())  # Should return an empty queryset
<QuerySet []>
