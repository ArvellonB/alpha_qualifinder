from django.db import models

# User model
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=100)
    headline = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
