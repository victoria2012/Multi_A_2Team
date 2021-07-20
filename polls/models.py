from django.db import models

# Create your models here.
class nmovie(models.Model):
    title = models.CharField(max_length=100)
    outline = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=20, decimal_places=5, default=0)
