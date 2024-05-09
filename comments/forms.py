from django import forms
from .models import Comment

# Form for creating a new comment on a post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Similar to PostForm, only the content is needed
