from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)  # For admin toggling

    def __str__(self):
        return self.title
