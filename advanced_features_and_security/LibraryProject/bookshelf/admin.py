from django.contrib import admin
from .models import CustomUser

# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(admin.ModelAdmin): 
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),  
    )

admin.site.register(CustomUser, CustomUserAdmin)