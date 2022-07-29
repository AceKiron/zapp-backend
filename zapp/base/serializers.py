from statistics import mode
from rest_framework import serializers

from . import models

        
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    musics=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=models.Album
        fields=('id','album_title','artist','genre','musics')

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    #album_title=serializers.CharField(source='album.album_title')
    class Meta:
        model=models.Music
        fields=('id','name','song','album')