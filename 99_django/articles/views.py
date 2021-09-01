from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)



def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 1. 사용자가 입력한 데이터 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. 가져온 데이터 저장하기
    article = Article()
    article.title = title
    article.content = content 
    article.save()

    # 3. index페이지로 리다이렉트 시킴
    return redirect('articles:index')

    # 왜 render를 안쓰고 redirect를 쓰나요?
    # => 중복된 코드가 이미 index함수에 있음
    # articles = Article.objects.all()
    # context = {
    #     'articles': articles
    # }
    # return render(request, 'articles/index.html', context)