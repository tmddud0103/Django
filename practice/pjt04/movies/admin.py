# articles/admin.py
from django.contrib import admin
from .models import Movie

# admin site에 등록(register)한다.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'overview', 'poster_path', 'created_at', 'updated_at']

admin.site.register(Movie, MovieAdmin)