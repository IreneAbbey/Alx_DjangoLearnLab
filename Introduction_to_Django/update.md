from bookshelf.models import Book  

# Retrieve the book to update  
book = Book.objects.get(id=1)  

# Update its attributes  
book.title = "Nineteen Eighty-Four"  
book.publication_year = 1950  

# Save the changes  
book.save()  

print(book)  
Expected Output:
<Book: Nineteen Eighty-Four>
