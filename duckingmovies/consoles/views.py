from django.shortcuts import render

from rest_framework import viewsets

from consoles.models import Console
from consoles.serializers import ConsoleSerializer
from permissions.services import APIPermissionClassFactory

# Create your views here.

class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ConsolePermission',
            permission_configuration={
                'base': {
                    'create': lambda user, requ: user.is_staff,
                    'list': True,
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
