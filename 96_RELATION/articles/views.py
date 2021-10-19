from django.shortcuts import redirect, render
from .models import Article
from .forms import CommentForm, ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        'article': article,
        'comment_form': comment_form,
    }

    return render(request, 'articles/detail.html', context)


def comments_create(request, pk):
    # article 인스턴스를 사용하는 방법
    # article = Article.objects.get(pk=pk)

    # comment_form = CommentForm(request.POST)

    # if comment_form.is_valid():
    #     comment = comment_form.save(commit=False)
    #     comment.article = article
    #     comment.save()

    # return redirect('articles:detail', pk)



    # article_id를 이용하는 방법
    article = Article.objects.get(pk=pk)

    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article_id = pk
        comment.user = request.user
        comment.save()

    return redirect('articles:detail', pk)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')

    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form, 
    }
    return render(request, 'articles/create.html', context)

