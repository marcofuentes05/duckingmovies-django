from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from permissions.services import APIPermissionClassFactory
# Create your views here.

from .models import Director
from .serializers import DirectorSerializer
from awards.serializers import AwardSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='DirectorPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, request: user.is_staff,
                    'list': lambda user, request: user.is_authenticated,
                    'directorAwards': lambda user, request: user.is_authenticated,
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

    @action(detail = True, url_path = 'awards' , methods = ['get'])
    def directorAwards(self, request, pk = None):
        awards = self.get_object().awards.all()
        return Response(
            AwardSerializer(award).data for award in awards
        )
