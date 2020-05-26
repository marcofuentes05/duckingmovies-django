
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory


from .models import Actor
from .serializers import ActorSerializer
from awards.serializers import AwardSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ActorPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, requ : user.is_staff,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': True,
                    'update': lambda user, req, third: user.is_authenticated,
                    'partial_update': True,
                    'destroy': lambda user, req, third: user.is_authenticated,
                    'actorAwards': lambda user, req, third: user.is_authenticated,
                }
            }
        ),
    )

    @action(detail = True, url_path = 'awards',methods = ['get'])
    def actorAwards(self, request, pk = None):
        awards = self.get_object().awards.all()
        return Response(
            AwardSerializer(award).data for award in awards
        )
