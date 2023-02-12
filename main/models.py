from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, name='title')
    anounce = models.CharField(max_length=100)
    text = models.TextField(name='text')
    author_id = models.IntegerField()
    date = models.DateTimeField()
    