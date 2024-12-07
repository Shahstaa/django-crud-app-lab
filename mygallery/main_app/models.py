from django.db import models
from django.contrib.auth.models import User

class Sculpture(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year_created = models.IntegerField()
    description = models.TextField()
    file = models.ImageField(upload_to='sculptures/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

