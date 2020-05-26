from django.shortcuts import render

from rest_framework import viewsets

from videogames.models import Videogame
from videogames.serializers import VideogameSerializer
from permissions.services import APIPermissionClassFactory

# Create your views here.

class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogame.objects.all()
    serializer_class = VideogameSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='VideogamePermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'update': True,
                    'partial_update': True,
                    'destroy': True,
                }
            }
        ),
    )