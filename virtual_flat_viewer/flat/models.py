from django.db import models
from cameras.models import camera
from house.models import house

# Create your models here.
class flat(models.Model):
    Titel = models.CharField(max_length=128)
    Stockwerk = models.CharField(max_length=128)
    Position = models.CharField(max_length=128)
    Expose = models.ImageField()
    Beschreibung = models.TextField()
    Bild = models.ImageField()
    Kameras = models.ManyToManyField(camera)
    Haus = models.ForeignKey(house)
    Fläche = models.CharField(max_length=32)
    Kaltmiete = models.CharField(max_length=32)
    Objektnummer = models.CharField(max_length=32)

    def __str__(self):
        return self.Titel
