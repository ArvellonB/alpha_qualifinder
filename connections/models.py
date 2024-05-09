from django.db import models
from users.models import User

# Connection model
class Connection(models.Model):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]

    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='initiator_connections')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_connections')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=PENDING)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1} - {self.user2} ({self.status})"
