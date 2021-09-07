from django import forms
from .models import Article

#article을 저장하기 위한 폼
class ArticleForm(forms.ModelForm):
    # 커스터마이징 참고용
    # title = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class' : 'form-control'
    #         }
    #     )
    # )

    class Meta():
        # 데이터를 손상하지 않고 새로운 공간에 데이터를 저장하는 방법
        # = 메타 데이터
        model = Article
        fields = '__all__'

