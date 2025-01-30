from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255, default="Unknown Location")
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)

    def __str__(self):
        return self.title
