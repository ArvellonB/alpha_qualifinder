from django.shortcuts import render
from .models import Message

# View for displaying messages between users
def user_messages(request, user_id):
    received_messages = Message.objects.filter(receiver_id=user_id)
    sent_messages = Message.objects.filter(sender_id=user_id)
    return render(request, 'user_messages/messages.html', {
        'received_messages': received_messages,
        'sent_messages': sent_messages
    })
