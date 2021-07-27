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