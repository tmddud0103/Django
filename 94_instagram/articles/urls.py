from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:pk>/likes/', views.likes, name='likes'),
]