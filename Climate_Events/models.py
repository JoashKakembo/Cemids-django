from django.db import models

class ClimateEvent(models.Model):
    event_title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='climate_event_images/', null=True, blank=True)
    event_date = models.DateField()
    event_time = models.TimeField()

    def __str__(self):
        return self.event_title


