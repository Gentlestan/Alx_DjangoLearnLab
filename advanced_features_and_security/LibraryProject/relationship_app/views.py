# from django.shortcuts import render, redirect, get_object_or_404 
# from .models import Book
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth import login, authenticate

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import permission_required
# from django.contrib.auth.decorators import login_required, user_passes_test

# from .models import UserProfile
# from .forms import BookForm  # ✅ Make sure you create this form if it doesn't exist








# # Function-based view to list all books
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})


# from django.shortcuts import render
# from django.views.generic.detail import DetailView
# from .models import Library

# # Class-based view to show library details
# class LibraryDetailView(DetailView):
#     model = Library  # Reference the Library model
#     template_name = 'relationship_app/library_detail.html'  # Template for displaying the library details
#     context_object_name = 'library'  # Use 'library' as the context variable name in the template


# # Registration View
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the user
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=password)  # Authenticate the user
#             login(request, user)  # Log the user in after registration
#             return redirect('home')  # Redirect to home or any other page
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# # These views are built-in
# class CustomLoginView(LoginView):
#     template_name = 'relationship_app/login.html'

# class CustomLogoutView(LogoutView):
#     template_name = 'relationship_app/logout.html'


# # Helper function to check roles
# def user_is_admin(user):
#     return user.userprofile.role == 'Admin'

# def user_is_librarian(user):
#     return user.userprofile.role == 'Librarian'

# def user_is_member(user):
#     return user.userprofile.role == 'Member'

# # Admin View
# @login_required
# @user_passes_test(user_is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# # Librarian View
# @login_required
# @user_passes_test(user_is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# # Member View
# @login_required
# @user_passes_test(user_is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')


# # Add Book View
# @permission_required('relationship_app.can_add_book', raise_exception=True)
# def add_book(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list_books')
#     else:
#         form = BookForm()
#     return render(request, 'relationship_app/book_form.html', {'form': form})

# # Edit Book View
# @permission_required('relationship_app.can_change_book', raise_exception=True)
# def edit_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     form = BookForm(request.POST or None, instance=book)
#     if form.is_valid():
#         form.save()
#         return redirect('list_books')
#     return render(request, 'relationship_app/book_form.html', {'form': form})

# # Delete Book View
# @permission_required('relationship_app.can_delete_book', raise_exception=True)
# def delete_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         book.delete()
#         return redirect('list_books')
#     return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})


from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def list_book(request):
     # Get all books and their authors
    books = Book.objects.select_related('author').all()
    
    # Build a simple text output
    output_lines = [f"{book.title} by {book.author.name}" for book in books]
    output_text = "\n".join(output_lines)
    
    # Return as plain text response
    return HttpResponse(output_text, content_type="text/plain")



class LibraryDetailView(DetailView):
    model = Library  # The model we’re showing details for
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # Name used in the template
