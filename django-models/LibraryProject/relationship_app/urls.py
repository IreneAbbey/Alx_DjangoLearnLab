from django.urls import path
from relationship_app.views import all_books, LibraryDetailView


urlpatterns = [
    path('books/', all_books, name='all_books'),
    path('library/<str:name>/', LibraryDetailView.as_view(), name='library_detail')
]
