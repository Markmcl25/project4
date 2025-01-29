from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
