from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory

from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                    'newUser': True
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

    @action(detail=False, url_path = 'create_user', methods = ['post'])
    def newUser (self, request):
        print(request.data)
        print(request.data['username'])
        usuario = User(
            username=request.data['username'], 
            first_name=request.data['firstName'],
            last_name=request.data['lastName'],
            email=request.data['email'], 
            is_staff = False
        )
        usuario.set_password(request.data['password'])
        usuario.save()
        return Response({
            'status':'ok'
        })
