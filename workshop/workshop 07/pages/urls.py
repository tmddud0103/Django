from django.urls import path
from . import views

urlpatterns = [
    path('dinner/<str:menu>/<int:num>', views.dinner, name='dinner')
]
