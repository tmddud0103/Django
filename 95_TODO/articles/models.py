from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.
class Article(models.Model):
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField()