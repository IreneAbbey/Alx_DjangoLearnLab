from .models import Book, Author
from rest_framework import serializers
import datetime

# Serializer for Book model with validation for publication year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year', 'author')

# Ensure the publication year is not in the future
    def validate_publication_year(self,value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

# Serializer for Author model with nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('name')