from django.db import models

# Create your models here.

# Model representing an author.
class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

# Model representing an book.
class Book(models.Model):
    title = models.CharField(max_length=250)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title