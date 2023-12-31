from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f' {self.name}'



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    coding_language = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.URLField()

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255)
    origin_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f' {self.author}: {self.comment}'
    

