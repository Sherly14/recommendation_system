from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Singer)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    listdisplay = ['song_name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    listdisplay = ['movie_name']
