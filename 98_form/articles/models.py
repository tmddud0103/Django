from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    # location = models.CharField(max_length=10)
    # user = models.CharField(max_length=10)
    # age = models.IntegerField()