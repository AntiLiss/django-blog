from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, name='title')
    anounce = models.CharField(max_length=100)
    text = models.TextField(name='text')
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    