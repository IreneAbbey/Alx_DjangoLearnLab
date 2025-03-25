from django.shortcuts import render
from rest_framework import viewsets, permissions
from.models import Like, Post, Comment
from.serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from notifications.models import Notification
from rest_framework.response import Response

# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserFeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user= request.user, post = post)
        if created:
            Notification.objects.create(recipients=post.author, actor = request.user, verb="liked your post",  target = post)
            return Response({"message": "Post Liked"}, status= status.HTTP_201_CREATED)
        else:
            return Response({"message": "Post Already Liked"}, status= status.HTTP_200_OK)
        

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(post_id=post_id)
            like = Like.objects.get(user= request.user, post = post)
            like.delete()
            return Response({"message": "Post Unliked"}, status= status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"message": "Post Not Liked"}, status= status.HTTP_200_OK)