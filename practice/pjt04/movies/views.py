from django.shortcuts import render, redirect
from .models import Movie


# Create your views here.
def index(request):
    search_word = request.GET.get('search', '')

    if not search_word:
        movies = Movie.objects.all()

    if search_word:
        total_movies = Movie.objects.all()
        # 검색 단어가 제목에 포함된 영화만 필터링
        movies = [movie for movie in total_movies if search_word in movie.title]
        # 필터링 결과 영화가 없으면
        if not movies:
            movies = total_movies
    
    context = {
        'movies' : movies
    }

    return render(request, 'movies/index.html', context)
# def index(request):
#     movies = Movie.objects.all()
#     context = {
#         'movies' : movies
#     }
#     return render(request, 'movies/index.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    movie = Movie(title=title, overview=overview, poster_path=poster_path)
    movie.save()
    return redirect('movies:index')

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:index', movie.pk)

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/edit.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    movie.title = title
    movie.overview = overview
    movie.poster_path = poster_path
    movie.save()
    return redirect('movies:detail', movie.pk)


