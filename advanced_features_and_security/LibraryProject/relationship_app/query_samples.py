import os
import django
import sys

# -------------------------------
# Add project root to Python path
# -------------------------------
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# -------------------------------
# Set the correct settings module
# Use the exact folder name: LibraryProject
# -------------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# -------------------------------
# Initialize Django
# -------------------------------
django.setup()

# -------------------------------
# Now import your models
# -------------------------------
from relationship_app.models import Author, Book, Library, Librarian

# -------------------------------
# Query all books by a specific author
# -------------------------------
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print("Author not found.")

# -------------------------------
# List all books in a library
# -------------------------------
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name}:")
        for book in books:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"No books found in library: {library_name}")

# -------------------------------
# Retrieve librarian for a specific library
# -------------------------------
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found.")
    except Librarian.DoesNotExist:
        print("Librarian not assigned to this library.")

# -------------------------------
# Test the functions
# -------------------------------
if __name__ == "__main__":
    get_books_by_author("John Doe")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
