from django.shortcuts import render

from rest_framework import viewsets

from videogames.models import Videogame
from videogames.serializers import VideogameSerializer
#TODO import permission

# Create your views here.

class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogame.objects.all()
    serializer_class = VideogameSerializer
    #TODO permission_classes