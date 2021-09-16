from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/form.html', context)
    

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form': form,
    }

    return render(request, 'articles/form.html', context)