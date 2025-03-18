from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User Registration Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# User Profile Update Form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

