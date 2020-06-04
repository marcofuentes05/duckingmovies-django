from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from videogames.models import Videogame
from videogames.serializers import VideogameSerializer
from permissions.services import APIPermissionClassFactory
from comments.serializers import GameCommentSerializer
from django.contrib.auth.models import User
from comments.models import GameComment
from django.contrib.auth.models import User
from developers.models import Developer
from consoles.models import Console
from consoles.serializers import ConsoleSerializer
from developers.serializers import DeveloperSerializer
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
                    'search': lambda user, request: user.is_authenticated,
                },
                'instance': {
                    'retrieve': True,
                    'update': True,
                    'partial_update': True,
                    'destroy': True,
                    'getTrending' : lambda user, request , third : user.is_authenticated,
                    'getTrendingall' : True,
                    'getComments': True ,#lambda user, request, third: user.is_authenticated,  # True,
                    'comment': True,
                    'getConsoles' : True,
                    'getDev' : True,
                }
            }
        ),
    )

    @action(detail = True , url_path = 'consoles' , methods = ['get'])
    def getConsoles(self , request , pk = None) :
        consolas = self.get_object().consoles.all()
        return Response(
            ConsoleSerializer(consola).data for consola in consolas
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

    @action(detail=False, url_path='search', methods=['GET'])
    def search(self, request):
        genero = request.META.get('HTTP_GENRE')
        rate = float(request.META.get('HTTP_RATING'))
        if(genero=='Ninguno'):
            videogames = Videogame.objects.filter(rating__lte=rate)
            return Response(
                VideogameSerializer(videogame).data for videogame in videogames
            )
        else:
            videogames = Videogame.objects.filter(genres__name__contains=genero).filter(rating__lte=rate)
            return  Response(
                VideogameSerializer(videogame).data for videogame in videogames
            )

    @action(detail=True, url_path='comment', methods=['post'])
    def comment(self, request, pk=None):
        user = User.objects.get(id=request.data['author'])
        comment = GameComment(author=user, text=request.data['text'])
        comment.save()
        self.get_object().comments.add(comment)
        self.get_object().save()
        return Response({
            'id': comment.id,
            'text': comment.text,
            'author': comment.author.id
        })

    @action(detail = True , url_path = 'developer' , methods = ['get'])
    def getDev( self, request , pk = None ):
        dev = self.get_object().developer
        return Response(
            DeveloperSerializer(dev).data
        )
