from django import forms
from .models import Post

# Form for creating a new post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  # Only include the content field; user and timestamp are automatically set
