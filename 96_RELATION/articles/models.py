from django.db import models
# from django.conf import settings
# Create your models here.
class Article(models.Model):
    # id =
    # pk =
    title = models.CharField(max_length=100)
    content = models.TextField()
    # user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # comments_set
    # 하나의 게시물로 들어가서 그 안에 달려있는 모든 댓글을 출력


class Comment(models.Model):
    # id = 
    # pk =
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id 를 장고가 새로 만들어 준다