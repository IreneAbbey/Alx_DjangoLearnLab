from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.
def all_books(request):
    books = Book.objects.all()
    return render(request, 'library/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"