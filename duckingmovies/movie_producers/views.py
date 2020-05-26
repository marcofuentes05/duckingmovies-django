from django.shortcuts import render

from rest_framework import viewsets

from movie_producers.models import MovieProducer
from movie_producers.serializers import MovieProducerSerializer
from permissions.services import APIPermissionClassFactory

# Create your views here.

class MovieProducerViewSet(viewsets.ModelViewSet):
    queryset = MovieProducer.objects.all()
    serializer_class = MovieProducerSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='MovieProducerPermission',
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