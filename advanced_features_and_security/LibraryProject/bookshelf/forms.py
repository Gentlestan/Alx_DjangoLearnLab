from django import forms
from .models import Book

# ALX requires ExampleForm to exist
class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]