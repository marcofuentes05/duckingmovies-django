from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory

from django.contrib.auth.models import User
from .serializers import UserSerializer
from movies.serializers import MovieSerializer
from series.serializers import SerieSerializer
from comments.models import MovieComment
from videogames.serializers import VideogameSerializer

from videogames.models import Videogame
from series.models import Serie
from movies.models import Movie
from comments.serializers import MovieComment , SerieComment , GameComment

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': lambda user , rec : user.is_staff,
                    'newUser': True,
                    'upgrade': lambda user, rec : user.is_staff,
                    'cmovies' : lambda user , rec: user.is_authenticated,
                    'cseries': lambda user, rec: user.is_authenticated,
                    'cgames': lambda user, rec: user.is_authenticated,
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

    @action(detail=False, url_path = 'create_user', methods = ['post'])
    def newUser (self, request):
        print(request.data)
        print(request.data['username'])
        usuario = User(
            username=request.data['username'], 
            first_name=request.data['firstName'],
            last_name=request.data['lastName'],
            email=request.data['email'], 
            is_staff = False
        )
        usuario.set_password(request.data['password'])
        usuario.save()
        return Response({
            'status':'ok'
        })

    @action(detail = True, url_path = 'upgrade_user', methods = ['post'])
    def upgrade(self, request, pk = None):
        user = User.objects.get(id = pk)
        print(str(user.username))
        print(str(user.password))
        user.is_staff = True
        user.save()
        return Response({
            'Status': 'ok'
        })

    @action(detail = True , url_path = 'commented_movies' , methods = ['get'])
    def cmovies( self , request , pk = None ):
        movies = Movie.objects.filter(comments__author__id = pk)
        print(str(movies))
        return Response(
            MovieSerializer(movie).data for movie in movies
        )

    @action(detail=True, url_path='commentedseries', methods=['get'])
    def cseries(self, request, pk=None):
        series = Serie.objects.filter(comments__author__id=pk)
        return Response(
            SerieSerializer(serie).data for serie in series
        )

    @action (detail = True , url_path = 'commentedgames' , methods = ['get'])
    def cgames(self, request, pk = None):
        games = Videogame.objects.filter(comments__author__id=pk)
        return Response(
            VideogameSerializer(game).data for game in games
        )
