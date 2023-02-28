from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Extend User model to add more fields
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(default='profile_pics/default_avatar.jpg', upload_to='profile_pics/')


# Simple article model
class Article(models.Model):
    title = models.CharField(max_length=120, name='title')
    anounce = models.CharField(max_length=220)
    text = models.TextField(name='text', null=True, blank=True)
    image = models.ImageField(name='image', null=True, blank=True, upload_to='model_images/')
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

