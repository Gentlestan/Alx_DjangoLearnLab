### 🔹 `update.md` (Update the book’s title)

# Update the Book title

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

#Output

book.title # "Nineteen Eighty-Four"
