from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), 
    path('<pk>/', views.detail, name = 'detail'),
    path('<pk>/comments/', views.comments_create, name='comments_create'),
]
