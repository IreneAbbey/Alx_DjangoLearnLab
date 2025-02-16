from bookshelf.models import Book  

# Retrieve the book to delete  
book = Book.objects.get(id=1)  

# Delete the book  
book.delete()  

print("Book deleted successfully.")  
Expected Output:
Book deleted successfully.
