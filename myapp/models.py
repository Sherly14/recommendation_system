from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    class Meta:
        abstract = True

class Singer(BaseModel): # Model 1
    singer_name = models.CharField(max_length=100)
    def __str__(self):
        return self.singer_name

class Song(BaseModel): # Model 2
    singer_name = models.ManyToManyField(Singer,related_name='singer_name1')
    # movie_name = models.ManyToManyField(Movie,related_name='song_name1')
    song_name = models.CharField(max_length=100)
    def __str__(self):
        return self.song_name

class Movie(BaseModel): # Model 3
    movie_name = models.CharField(max_length=100)
    song_name = models.ManyToManyField(Song)
    def __str__(self):
        return self.movie_name










   
    