from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory

from .models import Genre
from .serializers import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='GenrePermission',
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
