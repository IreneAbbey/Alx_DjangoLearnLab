import rest_framework
import rest_framework.serializers


class BookSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']