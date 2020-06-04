from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory

from .models import Serie
from .serializers import SerieSerializer
from actors.serializers import ActorSerializer
from awards.serializers import AwardSerializer
from directors.serializers import DirectorSerializer
from comments.serializers import SerieCommentSerializer
class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='SeriePermission',
            permission_configuration={
                'base': {
                    'create': lambda user, request: user.is_staff,
                    'list': lambda user, request: user.is_authenticated,
                    'search': lambda user, request: user.is_authenticated,
                },
                'instance': {
                    'retrieve': True,
                    'update': lambda user, request, third: user.is_staff,
                    'getTrending' : lambda user, request: user.is_authenticated,
                    'partial_update': True,
                    'destroy': lambda user, request, third: user.is_staff,
                    'serieDirector': lambda user, request, third: user.is_authenticated,
                    'serieActors': True,
                    'serieAwards': True,
                    'getTrendingall' : True,
                    'getComments' : True,
                    'getComments' : True,
                }
            }
        ),
    )

    @action(detail=True, url_path='director', methods=['get'])
    def serieDirector(self, request, pk=None):
        director = self.get_object().director
        return Response(
            DirectorSerializer(director).data
        )


    @action(detail=True, url_path='actors', methods=['get'])
    def serieActors(self, request, pk=None):
        actors = self.get_object().actors.all()
        return Response(
            ActorSerializer(actor).data for actor in actors
        )

    @action(detail=True, url_path='awards', methods=['get'])
    def serieAwards(self, request, pk=None):
        awards = self.get_object().awards.all()
        return Response(
            AwardSerializer(award).data for award in awards
        )

    @action(detail=False, url_path='trending', methods=['get'])
    def getTrending(self, request):
        actual = Serie.objects.all()[::-1]
        if (len(actual) >= 5):
            return Response (
                SerieSerializer(actual[i]).data for i in range(5)
            )
        else:
            return Response(
                SerieSerializer(serie).data for serie in actual
            )

    @action(detail=False, url_path='trendingall', methods=['get'])
    def getTrendingall(self, request):
        actual = Serie.objects.all()[::-1]
        return Response(
            SerieSerializer(serie).data for serie in actual
        )

    @action(detail=True, url_path='comments', methods=['get'])
    def getComments(self, request, pk=None):
        comments = self.get_object().comments.all()
        return Response(
            {'id': SerieCommentSerializer(comment).data['id'], 'comentario': SerieCommentSerializer(comment).data['text'], 'username': comment.author.username} for comment in comments
        )

    @action(detail=False, url_path='search', methods=['GET'])
    def search(self, request):
        genero = request.META.get('HTTP_GENRE')
        rate = float(request.META.get('HTTP_RATING'))
        if(genero=='Ninguno'):
            series = Serie.objects.filter(rating__lte=rate)
            return Response(
                SerieSerializer(serie).data for serie in series
            )
        else:
            series = Serie.objects.filter(genres__name__contains=genero).filter(rating__lte=rate)
            return  Response(
                SerieSerializer(serie).data for serie in series
            )
