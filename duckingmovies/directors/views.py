from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

from .models import Director
from .serializers import DirectorSerializer
from awards.serializers import AwardSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    @action(detail = True, url_path = 'awards' , methods = ['get'])
    def directorAwards(self, request, pk = None):
        awards = self.get_object().awards.all()
        return Response(
            AwardSerializer(award).data for award in awards
        )
