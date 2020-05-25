from django.shortcuts import render

from rest_framework import viewsets

from developers.models import Developer
from developers.serializers import DeveloperSerializer
#TODO import permission

# Create your views here.

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    # TODO permission_classes