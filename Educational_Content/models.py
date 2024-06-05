from django.db import models

class EducationalContent(models.Model):
    images = models.ImageField(upload_to='educational_content_images/', null=True, blank=True)
    author = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    readmore = models.TextField()

    def __str__(self):
        return self.subtitle
