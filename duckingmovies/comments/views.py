from django.shortcuts import render

from rest_framework import viewsets

from comments.models import GameComment, MovieComment, SerieComment
from comments.serializers import GameCommentSerializer, MovieCommentSerializer, SerieCommentSerializer
#TODO importe de permisos

# Create your views here.

class GameCommentViewSet(viewsets.ModelViewSet):
    queryset = GameComment.objects.all()
    serializer_class = GameCommentSerializer
    # TODO permission_classes

class MovieCommentViewSet(viewsets.ModelViewSet):
    queryset = MovieComment.objects.all()
    serializer_class = MovieCommentSerializer
    # TODO permission_classes

class SerieCommentViewSet(viewsets.ModelViewSet):
    queryset = SerieComment.objects.all()
    serializer_class = SerieCommentSerializer
    # TODO permission_classes
