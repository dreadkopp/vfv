from django.db import models
from cameras.models import camera

# Create your models here.
class flat(models.Model):
    Titel = models.CharField(max_length=128)
    Stockwerk = models.CharField(max_length=128)
    Position = models.CharField(max_length=128)
    Expose = models.ImageField()
    Kameras = models.ManyToManyField(camera)

    def __str__(self):
        return self.Titel
