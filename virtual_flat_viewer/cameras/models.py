from django.db import models

# Create your models here.
class camera(models.Model):
    Titel = models.CharField(max_length=128)
    URL = models.CharField(max_length=256)
    #position of marker on expose
    position_left = models.CharField(max_length=128, default="0")
    position_top = models.CharField(max_length=128, default="0")

    def __str__(self):
        return self.Titel
