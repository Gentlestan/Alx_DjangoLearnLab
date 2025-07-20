from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library

# Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library  # Reference the Library model
    template_name = 'relationship_app/library_detail.html'  # Template for displaying the library details
    context_object_name = 'library'  # Use 'library' as the context variable name in the template

