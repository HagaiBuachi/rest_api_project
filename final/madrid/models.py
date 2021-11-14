from django.db import models
from django.urls import reverse

class Footballer (models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(default='default.png', blank=True)





    def __str__(self):
        return self.name





