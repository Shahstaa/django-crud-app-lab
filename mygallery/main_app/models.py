from django.db import models

class Sculpture(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title
