from django.db import models
# from accounts.models import User
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # id = 
    # pk = 
    
    # 1:N 관계 설정
    # 가능하지만, 권장하지 않는 방법
    # user = models.ForeignKey(User)
    # 장고에서 권장하는 방법
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # settings.AUTH_USER_MODEL => 'account.User'라는 string값이 들어감
    title = models.CharField(max_length=100)
    content = models.TextField()
    # comment_set = 
    # 하나의 게시물로 들어가서 그 안에 달려있는 모든 댓글을 출력


class Comment(models.Model):
    # id = 
    # pk = 
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = 
