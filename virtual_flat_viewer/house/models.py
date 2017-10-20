from django.db import models
#from flat.models import flat

# Create your models here.

class house(models.Model):
    Titel = models.CharField(max_length=128)
    Straße = models.CharField(max_length=128)
    Hausnummer = models.CharField(max_length=8)
    PLZ = models.CharField(max_length=5)
    Ort = models.CharField(max_length=128)
    Bild = models.ImageField()
    Beschreibung = models.TextField()
    #Wohnungen = models.ManyToManyField(flat)

    def __str__(self):
        return self.Titel
