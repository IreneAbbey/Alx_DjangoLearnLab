from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from.models import CustomUser
from.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data}, status = status.HTTP_201_CREATED)
    
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': user.username}, status=status.HTTP_200_OK)
    return Response ({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def get_object(self):
        return self.request.user
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, user_id)
        request.user.following.add(user_to_follow)
        return Response(status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, user_id)
        request.user.following.remove(user_to_unfollow)
        return Response(status=status.HTTP_200_OK)