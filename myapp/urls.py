from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    # path('',views.index,name="home"),
    path('',views.home,name="home"),
    path('get_songs',views.get_songs,name="get_songs"),
    path('get_singers',views.get_singers,name="get_singers"),
    path('get_movies',views.get_movies,name="get_movies")
]