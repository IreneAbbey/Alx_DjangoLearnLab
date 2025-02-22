from django.urls import path
from .views import LoginView, LogoutView, list_books, LibraryDetailView, register  
from LibraryProject.relationship_app import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<str:name>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login_view'),  
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout_view'),  
    path('register/', views.register, name='register_view'), 
]
