from django.shortcuts import render

from rest_framework import viewsets

from consoles.models import Console
from consoles.serializers import ConsoleSerializer
#TODO import permission

# Create your views here.

class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    #TODO permission_classes