from django.db import models
from django.db.models.base import Model
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title

class Userdata(models.Model):
    name = models.CharField(max_length=200) 
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    gender = models.CharField(max_length=200) 
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)

# Create your models here.
