from django.db import models



# Create your models here.

class Movie(models.Model): # Model class 상속
    # id는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    title = models.CharField(max_length=100) # 클래스 변수(DB의 필드)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


