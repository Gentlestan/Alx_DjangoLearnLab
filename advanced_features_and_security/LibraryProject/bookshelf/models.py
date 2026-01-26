from django.db import models
from django.conf import settings  # ✅ use this to reference the user model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    # Reference the custom user as a foreign key
owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # points to CustomUser
        on_delete=models.CASCADE,   # if user is deleted, delete their books
        related_name="bookshelf_books",  # optional: lets you access user.books
        null=True,
        blank=True
    )

def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"