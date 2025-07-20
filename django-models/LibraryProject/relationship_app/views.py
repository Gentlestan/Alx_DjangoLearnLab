from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate

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


# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)  # Authenticate the user
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home or any other page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# These views are built-in
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'