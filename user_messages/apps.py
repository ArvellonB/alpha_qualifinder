# user_messages/apps.py
from django.apps import AppConfig

class UserMessagesConfig(AppConfig):
    name = 'user_messages'  # This should match the actual directory name of the app
    label = 'user_messages'  # Unique label to avoid conflict
