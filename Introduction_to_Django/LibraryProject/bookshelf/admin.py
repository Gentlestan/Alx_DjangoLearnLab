
# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the admin list view
    search_fields = ('title', 'author')  # Add a search box for title and author
    list_filter = ('publication_year',)  # Add a filter sidebar for publication year
