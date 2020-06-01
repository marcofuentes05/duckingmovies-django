from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory

from .models import Movie
from .serializers import MovieSerializer
from actors.serializers import ActorSerializer
from awards.serializers import AwardSerializer
from comments.models import MovieComment
from comments.serializers import MovieCommentSerializer
class MovieViewSet ( viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='MoviePermission',
            permission_configuration={
                'base': {
                    'create': lambda user, request, third: user.is_staff,
                    'list': lambda user, request: user.is_authenticated,
                    'getBanner' : True
                },
                'instance': {
                    'retrieve': True,
                    'update': True,
                    'partial_update': True,
                    'destroy': True,
                    'movieDirector': lambda user, request, third: user.is_authenticated,
                    'movieActors': lambda user, request, third: user.is_authenticated,
                    'movieAwards': lambda user, request, third: user.is_authenticated,
                    'getTrending' : True,
                    'getTrendingall' : True,
                    'getComments' : True

                }
            }
        ),
    )

    @action(detail = True, url_path = 'director', methods = ['get'])
    def movieDirector(self, request, pk = None):
        director = self.get_object().director
        return Response({
            str(director)
        })

    @action(detail = True, url_path = 'actors', methods = ['get'])
    def movieActors(self, request, pk = None):
        actors = self.get_object().actors.all()
        return Response(
            ActorSerializer(actor).data for actor in actors
        )

    @action(detail=True, url_path='awards', methods=['get'])
    def movieAwards(self, request, pk = None):
        awards = self.get_object().award.all()
        return Response(
            AwardSerializer(award) for award in awards
        )

    @action(detail = False , url_path='banner' ,  methods = ['get'])
    def getBanner(self , request ):
        movie = Movie.objects.all()[::-1]
        return Response(
            MovieSerializer(movie[0]).data
        )

    @action (detail = False , url_path = 'trending' , methods = ['get'])
    def getTrending ( self, request ): 
        actual = Movie.objects.all()[::-1]
        # actual = movies[::-1]
        if len(actual) >= 5:
            return Response(
                MovieSerializer(actual[m]).data for m in range(5)
            )
        return Response(
            MovieSerializer(actual[m]).data for m in range(len(actual))
        )

    @action(detail=False, url_path='trendingall', methods=['get'])
    def getTrendingall(self, request):
        actual = Movie.objects.all()[::-1]
        return Response(
            MovieSerializer(act).data for act in actual
        )

    @action(detail = True , url_path = 'comments' , methods = ['get'])
    def getComments(self, request , pk = None):
        comments = self.get_object().comments.all()
        return Response(
            MovieCommentSerializer(comment).data for comment in comments
        )