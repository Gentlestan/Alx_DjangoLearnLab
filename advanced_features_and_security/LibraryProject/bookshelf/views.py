from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["title"],
            author=request.POST["author"],
            publication_year=request.POST["year"],
            owner=request.user
        )
        return redirect("book_list")
    return render(request, "bookshelf/create_book.html")


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST["title"]
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/edit_book.html", {"book": book})


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect("book_list")