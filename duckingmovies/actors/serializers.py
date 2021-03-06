from rest_framework import serializers

from actors.models import Actor
from awards.serializers import AwardSerializer

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'id',
            'name',
            'lastName',
            'birthDate',
            'birthPlace',
            'netWorth',
            'height',
            'nickname',
            'awards'
        )
