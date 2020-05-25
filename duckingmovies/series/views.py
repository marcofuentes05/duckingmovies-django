from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Serie
from .serializers import SerieSerializer
from actors.serializers import ActorSerializer
from awards.serializers import AwardSerializer
class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

    @action(detail=True, url_path='director', methods=['get'])
    def serieDirector(self, request, pk=None):
        director = self.get_object().director
        return Response({
            str(director)
        })


    @action(detail=True, url_path='actors', methods=['get'])
    def serieDirector(self, request, pk=None):
        actors = self.get_object().actors.all()
        return Response(
            ActorSerializer(actor).data for actor in actors
        )

    @action(detail=True, url_path='awards', methods=['get'])
    def serieAwards(self, request, pk=None):
        awards = self.get_object().awards.all()
        return Response(
            AwardSerializer(award) for award in awards
        )
