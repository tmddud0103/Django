from django.shortcuts import redirect, render
from .models import Article
from .forms import CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)

def comments_create(request, pk):
    #article를 이용하는 방법
    # article = Article.objects.get(pk=pk)

    # comment_form = CommentForm(request.POST)
    # if comment_form.is_valid():
    #     comment = comment_form.save(commit=False)
    #     comment.article = article
    #     comment.save()

    # return redirect('articles:detail', pk)


    #article_id를 이용하는 방법
    # article = Article.objects.get(pk=pk)

    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article_id = pk
        comment.save()

    return redirect('articles:detail', pk)