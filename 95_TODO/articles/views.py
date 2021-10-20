from django.shortcuts import redirect, render
from .forms import ArticleForm
# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            # auther에 대한 정보가 없으니 임시 저장 후(commit=False)
            article = form.save(commit=False)
            # auther에 user를 저장
            article.auther = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form' : form
    }

    return render(request, 'articles/form.html', context)