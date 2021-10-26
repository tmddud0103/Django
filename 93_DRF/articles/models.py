from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=CASCADE)
    content = models.CharField(max_length=50)