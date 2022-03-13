from django.shortcuts import render,HttpResponse
from .models import *

def get_songs(request):
    id = request.GET["id"]
    try:
        filtered_songs = Song.objects.filter(singer_name=id)
        
        result = {
            'filtered_songs': filtered_songs,
            'singers' : Singer.objects.all(),
            'songs' : Song.objects.all(),
            'movies' : Movie.objects.all(),
            'colors' : ['primary','secondary','success']
        }
    except Song.DoesNotExist:
        filtered_songs = None
    return render(request,"myapp/index.html",result)

def home(request):
    dict = {
        'singers' : Singer.objects.all(),
        'songs' : Song.objects.all(),
        'movies' : Movie.objects.all()
    }
    return render(request,"myapp/index.html",context=dict)

def get_singers(request):
    id = request.GET["id"]
    try:
        filtered_songs = Song.objects.get(pk=id)
        filtered_singers = filtered_songs.singer_name.all()
        filtered_movies = Movie.objects.filter(song_name=filtered_songs)
        # filtered_movies = filtered_songs.movie_name.all()
        result = {
            'filtered_songs': Song.objects.all(),
            'filtered_singers': filtered_singers,
            'filtered_movies': filtered_movies,
            'singers' : Singer.objects.all(),
            'songs' : Song.objects.all(),
            'movies' : Movie.objects.all(),
            'colors' : ['primary','secondary','success']
        }
    except Song.DoesNotExist:
        filtered_singers = None
    return render(request,"myapp/index.html",result)

def get_movies(request):
    id = request.GET["id"]
    try:
        filtered_movie = Movie.objects.get(pk=id)
        print("Movie : ",filtered_movie)
        filtered_songs = filtered_movie.song_name.all()
        print("Songs : ",filtered_songs)
        result = {
            'filtered_songs': filtered_songs,
            'singers' : Singer.objects.all(),
            'songs' : Song.objects.all(),
            'movies' : Movie.objects.all(),
            'colors' : ['primary','secondary','success']
        }
    except Song.DoesNotExist:
        filtered_songs = None
    return render(request,"myapp/index.html",result)
