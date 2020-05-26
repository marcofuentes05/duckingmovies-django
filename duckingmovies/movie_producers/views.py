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
                    'create': lambda user, request: user.is_staff,
                    'list': lambda user, request: user.is_authenticated,
                },
                'instance': {
                    'retrieve': True,
                    'update': lambda user, request, third: user.is_staff,
                    'partial_update': True,
                    'destroy': lambda user, request, third: user.is_staff,
                }
            }
        ),
    )
