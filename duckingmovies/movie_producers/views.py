from django.shortcuts import render

from rest_framework import viewsets

from movie_producers.models import MovieProducer
from movie_producers.serializers import MovieProducerSerializer

# Create your views here.

class MovieProducerViewSet(viewsets.ModelViewSet):
    queryset = MovieProducer.objects.all()
    serializer_class = MovieProducerSerializer
    #TODO permission_classes