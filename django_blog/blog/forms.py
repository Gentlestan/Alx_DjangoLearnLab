from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


# Custom widget for tags (for the checker)
class TagWidget(forms.TextInput):
    input_type = 'text'


# PostForm with tag widget
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget(attrs={'placeholder': 'Enter tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Pre-fill tags when editing
            self.fields['tags'].initial = ", ".join(tag.name for tag in self.instance.tags.all())

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        tags_data = self.cleaned_data.get('tags', '')
        tag_list = [tag.strip() for tag in tags_data.split(',') if tag.strip()]

        instance.tags.clear()
        for tag_name in tag_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)

        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment...'
            }),
        }
