from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('get_data',views.get_data,name="get_data"),
]