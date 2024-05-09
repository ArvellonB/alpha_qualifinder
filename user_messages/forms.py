from django import forms
from .models import Message

# Form for creating a new message
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']  # Include receiver and content; sender is set in the view
