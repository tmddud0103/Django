from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = '__all__'
        # article이라는 필드는 읽기 전용 필드이다를 선언
        read_only_fields = ('article', )

# 게시물들과 함께 댓글까지 함께 출력
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta():
        model = Article
        fields = '__all__'

# 게시물들만 출력
class ArticleListSerializer(serializers.ModelSerializer):
    # 한개의 게시물이 가지고 있는 전체 댓글의 갯수 출력
    # case2 - Nested relation
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta():
        model = Article
        fields = '__all__'