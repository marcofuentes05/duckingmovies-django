from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Actor
from .serializers import ActorSerializer
from awards.serializers import AwardSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail = True, url_path = 'awards',methods = ['get'])
    def actorAwards(self, request, pk = None):
        awards = self.get_object().awards.all()
        return Response(
            AwardSerializer(award).data for award in awards
        )