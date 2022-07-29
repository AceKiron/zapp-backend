from django.db import models

class Album(models.Model):
    artist=models.CharField(max_length=200)
    album_title=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.album_title

# Create your models here.
class Music(models.Model):
    name=models.CharField(max_length=200)
    album=models.ForeignKey(Album,related_name='musics',on_delete=models.CASCADE)
    song=models.FileField(upload_to="songs/")
    def __str__(self) -> str:
        return self.name
