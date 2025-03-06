from django.shortcuts import render
import rest_framework
from api.models import Book
from api.serializers import BookSerializer

# Create your views here.
class BookList(rest_framework.generic.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

