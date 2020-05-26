from django.shortcuts import render

from rest_framework import viewsets

from developers.models import Developer
from developers.serializers import DeveloperSerializer
from permissions.services import APIPermissionClassFactory

# Create your views here.

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='DeveloperPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, request: user.is_staff,
                    'list': lambda user, request: user.is_authenticated,
                },
                'instance': {
                    'retrieve': True,
                    'update': lambda user, request, third: user.is_staff,
                    'partial_update': True,
                    'destroy': lambda user, request, third: user.is_staff,
                }
            }
        ),
    )
