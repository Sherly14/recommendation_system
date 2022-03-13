from django.shortcuts import render,HttpResponse
from .models import *

def get_data(request):
    id = request.GET["id"]
    para = request.GET["para"]

    filtered_songs = ""
    songs = Song.objects.all()
    singers  = Singer.objects.all()
    movies = Movie.objects.all()

    try:

        if para == "singer" :   
        
            filtered_songs = Song.objects.filter(singer_name=id)
            songs = filtered_songs if filtered_songs else songs
           
        elif para == "song":
        
            filtered_songs = Song.objects.get(pk=id)
            filtered_singers = filtered_songs.singer_name.all()
            filtered_movies = Movie.objects.filter(song_name=filtered_songs)        
            singers = filtered_singers if filtered_songs else singers
            movies = filtered_movies if filtered_songs else movies
        
        elif para == "movie":
        
            filtered_movie = Movie.objects.get(pk=id)
            filtered_songs = filtered_movie.song_name.all()
            songs = filtered_songs if filtered_songs else songs
        
    except Exception as ex:
            print("Exception : ",ex)   

    result = {
            'singers' : singers,
            'songs' : songs,
            'movies' : movies,
        }
    
    return render(request,"myapp/index.html",result)

def home(request):
    
    result = {
        'singers' : Singer.objects.all(),
        'songs' : Song.objects.all(),
        'movies' : Movie.objects.all()
    }
    return render(request,"myapp/index.html",result)

