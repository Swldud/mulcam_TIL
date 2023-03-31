from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    #Timestamp
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 


def __str__(self):
    # <Article #1 : 안녕하세요>
    return f'#{self.pk}: {self.title}'