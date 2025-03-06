from django.shortcuts import render
import rest_framework
from rest_framework import generics
from api.models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.
class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

