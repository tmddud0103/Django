from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        # exclude = ('article',)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields='__all__'
        exclude = ('user', )