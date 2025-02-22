from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, register_view


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<str:name>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login', login_view, name='login_view'),
    path('logout', logout_view, name='logout_view'),
    path('register', register_view, name='register_view'),
]
