from django.urls import path
from .views import LoginView, LogoutView, LibraryDetailView
from .views import list_books
from LibraryProject.relationship_app import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<str:name>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login_view'),  
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout_view'),  
    path('register/', views.register, name='register_view'),
    path('admin/', views.adminView, name='admin_view'),
    path('librarian/', views.librarianView, name='librarian_view'),
    path('member/', views.memberView, name='member_view'), 
    path('add_book/', views.add_book, name='add_book_view'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book_view'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book_view'),  # Add your paths here.
]
