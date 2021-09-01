from django.urls import path
# from articles import views 
from . import views

app_name = 'articles'

urlpatterns = [
    
    path('index/', views.index, name="index"),
    path('greeting/', views.greeting, name="greeting"), 
    path('dinner/', views.dinner, name="dinner"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    # url(링크)은 하이픈(-)으로 구별
    # 이유 : 링크를 복사붙여넣기(파란색+밑줄링크)를 하면 구별하기 어렵기 때문
    path('fake-google/', views.fake_google, name="fake_google"),
    # variabel routing
    path('hello/<int:name>/', views.hello, name="hello"),
    # path('hello/<name>/', views.hello),
]
