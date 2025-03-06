from django.shortcuts import render
import rest_framework
from rest_framework import generics
from api.models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

