from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Login View
def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user)
            return redirect("home")  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})



# Logout View
def LogoutView(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.get_user())
            return redirect("home")
        else:
            form = UserCreationForm()
            return render(request, "relationship_app/register.html", {"form": form})

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'admin'


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'member'

@user_passes_test(is_admin)
def adminView(request):
    return render(request, "relationship_app/admin.html")

@user_passes_test(is_librarian)
def librarianView(request):
    return render(request, "relationship_app/librarian.html")
   

@user_passes_test(is_member)
def memberView(request):
    return render(request, "relationship_app/member.html")
