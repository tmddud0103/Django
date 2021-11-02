from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, Comment
from articles.forms import ArticleForm, CommentForm
from django.http import JsonResponse

# Create your views here.
def index(request):
    articles = Article.objects.all()
    form = CommentForm()
    context =  {
        'articles': articles, 
        'form' : form,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)


def comments_create(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article_id = pk
        comment.save()
        return redirect('articles:index')


def likes(request, pk):
    user = request.user
    if user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if user in article.like_users.all():
            article.like_users.remove(user)
            liked = False
        else:
            article.like_users.add(user)
            # user.like_articles.add(article)
            liked = True
        context = {
            'liked' : liked,
            'count' : article.like_users.count(),
        }
        # return redirect('articles:index')
        return JsonResponse(context)

    return redirect('articles:index')
