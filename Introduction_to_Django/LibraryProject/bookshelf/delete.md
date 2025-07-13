### 🔹 `delete.md` (Delete the book and verify)

# Delete the Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

Output

(<QuerySet []>,)
