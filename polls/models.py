from django.db import models

# Create your models here.
class nmovie(models.Model):
    title = models.CharField(max_length=100)
    code = models.DecimalField(max_digits=20, decimal_places=5, default=0)
    genre = models.CharField(max_length=100)
    nation = models.CharField(max_length=100, default=0)
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)


class MovieRanking(models.Model):
    ranking = models.DecimalField(max_digits=20, decimal_places=5, default=0)
    title = models.CharField(max_length=100)