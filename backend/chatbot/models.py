from django.db import models
from django.contrib.auth.models import User  # Import the User model if needed
import random
import string
from datetime import timedelta
from django.utils import timezone

class ChatMessage(models.Model):
    # If you have user authentication, you can link messages to a user
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    is_user = models.BooleanField(default=False)  # True if the message is from the user
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'User' if self.is_user else 'Bot'}: {self.text[:50]}..."

# You can define other models below this one if needed

def generate_otp():
    return ''.join(random.choice(string.digits) for _ in range(4))

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.user.email}"

    def save(self, *args, **kwargs):
        self.otp = generate_otp()
        super().save(*args, **kwargs)

    def is_valid(self):
        # OTP is valid for 5 minutes (adjust as needed)
        return timezone.now() < self.created_at + timezone.timedelta(minutes=5)