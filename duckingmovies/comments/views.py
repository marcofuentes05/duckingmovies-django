from django.shortcuts import render

from rest_framework import viewsets

from comments.models import GameComment, MovieComment, SerieComment
from comments.serializers import GameCommentSerializer, MovieCommentSerializer, SerieCommentSerializer
from permissions.services import APIPermissionClassFactory

# Create your views here.

class GameCommentViewSet(viewsets.ModelViewSet):
    queryset = GameComment.objects.all()
    serializer_class = GameCommentSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='GameCommentPermission',
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

class MovieCommentViewSet(viewsets.ModelViewSet):
    queryset = MovieComment.objects.all()
    serializer_class = MovieCommentSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='MovieCommentPermission',
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

class SerieCommentViewSet(viewsets.ModelViewSet):
    queryset = SerieComment.objects.all()
    serializer_class = SerieCommentSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='SerieCommentPermission',
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
