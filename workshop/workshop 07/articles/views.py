from django.shortcuts import redirect, render
from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles' : articles
    }
    
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 1. 사용자 데이터 가져오기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. DB에 저장하기
    Article.objects.create(title=title, content=content)

    # 3. index로 보내주기
    return redirect('articles:index')


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    # 지울 article 찾기
    article = Article.objects.get(pk=pk)  

    # post로 들어왔다 => django가 만든 페이지에서 삭제 요청
    if request.method == 'POST':
        # 찾은 article 지우기
        article.delete()
        # 지운 후 index로 복귀
        return redirect('articles:index')
    # url에 delete를 붙여서 get으로 요청함
    else:
        # 정상적인 요청이 아니니 detail로 보내줄꼐
        return redirect('articles:detail', article.pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 기존 정보
    article =Article.objects.get(pk=pk)
    # 새로운 정보
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 수정 
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article.pk)