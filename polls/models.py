from django.db import models

# Create your models here.
class MovieRanking(models.Model):
    ranking = models.DecimalField(max_digits=20, decimal_places=5, default=0)
    title = models.CharField(max_length=100)
    
class MovieReview(models.Model):
    title = models.CharField(max_length=100)
    code = models.DecimalField(max_digits=20, decimal_places=5, default=0)
    score = models.DecimalField(max_digits=20, decimal_places=5, default=0)
    author = models.CharField(max_length=100)

class NaverMovie(models.Model):
    code = models.DecimalField(max_digits=20, decimal_places=5, default=False)
    author = models.CharField(max_length=90)
    rating = models.DecimalField(max_digits=20, decimal_places=5, default=False)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)