from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)  # Title of the event
    description = models.TextField()  # Detailed description of the event
    event_date = models.DateField()  # Date of the event
    event_time = models.TimeField()  # Time of the event
    location = models.CharField(max_length=100)  # Location of the event
    image = models.ImageField(upload_to='event_images/')  # Image of the event

    def __str__(self):
        return self.title

