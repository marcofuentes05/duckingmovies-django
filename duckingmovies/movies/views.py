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
                    'getBanner' : True,
                    'search': lambda user, request: user.is_authenticated,
                },
                'instance': {
                    'retrieve': True,
                    'update': True,
                    'getTrending' : lambda user, request: user.is_authenticated,
                    'partial_update': True,
                    'destroy': True,
                    'movieDirector': lambda user, request, third: user.is_authenticated,
                    'movieActors': True,
                    'movieAwards': True,
                    'getTrendingall' : True,
                    'getComments' : True,

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
            AwardSerializer(award).data for award in awards
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
            { 'id' : MovieCommentSerializer(comment).data['id'] , 'comentario' : MovieCommentSerializer(comment).data['text'] , 'username' : comment.author.username}  for comment in comments
        )

    @action(detail=False, url_path='search', methods=['GET'])
    def search(self, request):
        genero = request.META.get('HTTP_GENRE')
        rate = float(request.META.get('HTTP_RATING'))
        print(rate)
        print(genero)
        if(genero=='Ninguno'):
            movies = Movie.objects.filter(rating__lte=rate)
            return Response(
                MovieSerializer(movie).data for movie in movies
            )
        else:
            movies = Movie.objects.filter(genres__name__contains=genero).filter(rating__lte=rate)
            return  Response(
                MovieSerializer(movie).data for movie in movies
            )