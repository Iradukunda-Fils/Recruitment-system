from django.db import models
from applications.models import Applicant


# Create your models here.

class Notification(models.Model):
    # The user who receives the notification
    recipient = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="notifications")
    
    # Message or content of the notification
    message = models.TextField()
    
    # A flag to indicate if the notification has been read
    is_read = models.BooleanField(default=False)
    
    # Timestamp of when the notification was created
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient} - {self.message[:30]}..."  # Display part of the message for readability