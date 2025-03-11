from django.db import models

# Create your models here.

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() 

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField(null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)