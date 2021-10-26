from django.http import request
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.serializers import Serializer
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, Comment

# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    # GET /api/v1/articles/ => 전체 데이터 조회
    if request.method == 'GET':
        # Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True) # 쿼리셋을 넣었기 때문에 many값을 넣음
        return Response(serializer.data)

    # POST /api/v1/articles/ => 게시물 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article) # 단일 인스턴스를 넣었기 때문에 many값을 넣을 필요 없다
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'message' : 'delete done',
        }
        return Response(data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # commit=False 대신 밑의 방법을 사용해도 가능
        serializer.save(article=article)
        return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
