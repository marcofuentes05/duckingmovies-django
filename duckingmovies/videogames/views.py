from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from videogames.models import Videogame
from videogames.serializers import VideogameSerializer
from permissions.services import APIPermissionClassFactory
from comments.serializers import GameCommentSerializer
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
                    'getTrending' : True,
                    'getTrendingall' : True,
                    'getComments' : True
                }
            }
        ),
    )

    @action(detail=False, url_path='trending', methods=['get'])
    def getTrending(self, request):
        actual = Videogame.objects.all()[::-1]
        if (len(actual) >= 5):
            return Response(
                VideogameSerializer(actual[i]).data for i in range(5)
            )
        else:
            return Response(
                VideogameSerializer(serie).data for serie in actual
            )

    @action(detail=False, url_path='trendingall', methods=['get'])
    def getTrendingall(self, request):
        actual = Videogame.objects.all()[::-1]
        return Response(
            VideogameSerializer(serie).data for serie in actual
        )

    @action(detail=True, url_path='comments', methods=['get'])
    def getComments(self, request, pk=None):
        comments = self.get_object().comments.all()
        return Response(
            GameCommentSerializer(comment).data for comment in comments
        )
