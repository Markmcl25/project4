from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255, default="Untitled Event")
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255, default="Unknown Location")
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)
    category = models.CharField(max_length=100, default="General")

    def __str__(self):
        return self.title
