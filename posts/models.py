from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=500, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=20)
    posts = models.ManyToManyField(Post, blank=True)

