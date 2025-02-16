from bookshelf.models import Book  

# Retrieve all books  
books = Book.objects.all()  
print(books)  

# Retrieve a specific book by ID  
book = Book.objects.get(id=1)  
print(book)  

# Retrieve books with specific criteria  
books_by_author = Book.objects.filter(author="George Orwell")  
print(books_by_author)  
Expected Output:<QuerySet [<Book: 1984>, <Book: Animal Farm>]>
<Book: 1984>
<QuerySet [<Book: 1984>]>

