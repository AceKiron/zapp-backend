from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .import models
from . import serializers
class MusicViewSet(viewsets.ModelViewSet):
    queryset=models.Music.objects.all().order_by('id')
    serializer_class=serializers.MusicSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset=models.Album.objects.all().order_by('album_title')
    serializer_class=serializers.AlbumSerializer