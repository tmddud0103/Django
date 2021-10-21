from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    # user라는 모델과 user라는 모델(self)을 N대N으로 연결한다
    # 역참조를 할 때 저장하는 이름을 바꾸기 위해서 related_name을 사용
    # 내가 팔로우 하는 사람들의 목록
    # symmetrical => 자동 참조?
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # 나를 팔로우 하는 사람들의 목록
    #followers(user_set 대신 사용, related_name으로 인해 생성이 된다.)
    image = ProcessedImageField(upload_to='avatars',
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 60})