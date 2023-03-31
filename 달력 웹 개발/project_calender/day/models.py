from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    memo = models.CharField(max_length=100)

    #Timestamp
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
