from.models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'title', 'content', 'created_at', 'updated_at']