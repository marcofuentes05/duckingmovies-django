from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory

from .models import Award
from .serializers import AwardSerializer
# Create your views here.

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='AwardPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_staff,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': True,
                    'update': lambda user, req, third: user.is_staff,
                    'partial_update': True,
                    'destroy': lambda user, req, third: user.is_staff,
                }
            }
        ),
    )
