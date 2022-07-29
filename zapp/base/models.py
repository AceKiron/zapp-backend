from django.db import models

class Album(models.Model):
    artist=models.CharField(max_length=200)
    album_title=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)

# Create your models here.
class Music(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    song=models.FileField(upload_to="songs/")
