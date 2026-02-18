from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag

# -------------------------
# Authentication Forms
# -------------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


# -------------------------
# Custom Tag Widget
# -------------------------
class TagWidget(forms.TextInput):
    """Custom widget to input tags as comma-separated values."""
    input_type = 'text'


# -------------------------
# Post Form
# -------------------------
class PostForm(forms.ModelForm):
    # Explicitly use TagWidget() here
    tags = forms.CharField(
        required=False,
        widget=TagWidget(attrs={'placeholder': 'Enter tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags in Meta

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill tags when editing
        if self.instance.pk:
            self.fields['tags'].initial = ", ".join(tag.name for tag in self.instance.tags.all())

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        tags_data = self.cleaned_data.get('tags', '')
        tag_list = [tag.strip() for tag in tags_data.split(',') if tag.strip()]

        # Clear existing tags
        instance.tags.clear()
        for tag_name in tag_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)

        return instance


# -------------------------
# Comment Form
# -------------------------
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
