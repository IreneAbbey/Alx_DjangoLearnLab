import rest_framework


class BookSerializer(rest_framework.serializer.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']