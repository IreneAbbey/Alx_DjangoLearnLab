from django.urls import path
from .views import LoginView, LogoutView, list_books, LibraryDetailView, register  # Removed unnecessary views import

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<str:name>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login_view'),  # Fixed template_name syntax
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout_view'),  # Fixed template_name syntax
    path('register/', register, name='register_view'),  # Fixed trailing slash
]
