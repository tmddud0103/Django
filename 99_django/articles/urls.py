from django.urls import path
# from articles import views
from . import views

app_name = 'articles'

urlpatterns = [
    # 모든 article을 보여주는 페이지
    path('', views.index, name='index'),
    # 하나의 article을 보여주는 페이지
    path('<int:pk>/', views.detail, name='detail'),
    # 사용자가 데이터를 입력 할 수 있도록 빈 종이를 보여주는 페이지
    path('new/', views.new, name='new'),
    # 사용자가 입력한 데이터를 받아와서 DB에 저장하는 로직
    path('create/', views.create, name='create'),
    
]