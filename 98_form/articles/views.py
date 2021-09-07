from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import ArticleForm
from .models import Article

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# GET, HEAD만 받는 require_safe
@require_safe
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context ={
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    # 5. create 경로로 요청이 들어옴(POST) => '잘못된' 데이터를 담아서 저장해달라고 요청
    # 10. create 경로로 요청이 들어옴(POST) => 올바른 데이터를 담아서 저장해달라고 요청
    if request.method == 'POST':
        # 6. ArticleForm을 인스턴스화 한다. (사용자가 입력한 정보를 담아서)
        #    => 데이터가 입력된 종이 생성
        # 11. ArticleForm을 인스턴스화한다. (사용자가 입력한 정보를 담아서)
        #    => 데이터가 입력된 종이 생성
        form = ArticleForm(request.POST)
        # 7. 데이터가 유효한지 검증을 한다. (잘못된 데이터를 넣었기 때문에 실패)
        # 12. 데이터가 유요한지 검증을 한다. (올바른 데이터를 넣었기 때문에 성공)
        if form.is_valid():
            # 13. 데이터를 저장한다.
            form.save()
            # 14. index로 리다이렉트 시켜준다.
            return redirect('articles:index')
    # 1. create경로로 요청이 들어옴 (GET) => 빈 종이를 달라고 하는 요청
    else:
        # 2. ArticleForm을 인스턴스화 한다. => 빈 종이를 생성
        form = ArticleForm()
    # 3. 사용자에게 빈 종이를 주기 위해 context에 담는다.
    # 8. 유효한 데이터만 들어있는 종이를 다시 돌려주기 위해 context에 담는다.
    context = {
        'form' : form,
    }
    # 4. 사용자에게 빈 종이를 넘겨준다.
    # 9. 사용자에게 올바른 데이터가 있는 종이를 넘겨준다.
    return render(request, 'articles/form.html', context)
        

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # 0. 기존 정보를 가져온다.
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    # 5. update 요청이 들어옴 (POST) => 잘못된 데이터를 담아서 수정해달라고 요청
    # 10. update 요청이 들어옴(POST) => 올바른 데이터를 담아서 수정해달라고 요청
    if request.method == 'POST':
        # 6. ArticleForm을 인스턴스화 한다. (사용자가 수정한 정보 + 기존 정보)
        # 11. ArticleForm을 인스턴스화 한다. (사용자가 수정한 정보 + 기존 정보)
        form = ArticleForm(request.POST, instance = article)
        # 7. 데이터가 유효한지 검증을 한다. (잘못된 정보가 들어옴)
        # 12. 데이터가 유효한지 검증을 한다. (올바른 정보가 들어옴)
        if form.is_valid():
            # 13. 데이터를 수정한다.
            form.save()
            # 14. index로 리다이렉트 시켜준다.
            return redirect('articles:index')
    # 1. update요청이 들어옴 (GET) => 기존의 정보를 담은 종이를 요청
    else:
        # 2. 기존의 정보를 담은 종이를 생성
        form = ArticleForm(instance = article)
    # 3. 사용자에게 보여주기 위해 context에 저장
    # 8. 잘못 된 정보 중 유효한 데이터만 들어있는 종이를 다시 돌려주기 위해 context에 저장
    context = {
        'form' : form,
    }
    # 4. 사용자에게 종이를 보여준다.
    # 9. 사용자에게 올바른 데이터가 있는 종이를 넘겨준다.
    return render (request, 'articles/form.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()

    return redirect('articles:index')