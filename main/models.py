from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Extend User model to add more fields
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(default='profile_pics/default_avatar.jpg', upload_to='profile_pics/')


# Simple article model
class Article(models.Model):
    title = models.CharField(max_length=50, name='title')
    anounce = models.CharField(max_length=100)
    text = models.TextField(name='text')
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='model_images/')
