from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # 권장사항은 아님
        # model = User

        # 권장사항
        # getusermodel이 자동으로 User를 찾아줌
        model = get_user_model()