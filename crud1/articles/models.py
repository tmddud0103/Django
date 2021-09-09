from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Article(models.Model):
    image = ProcessedImageField(upload_to='image/',
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 100})
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)