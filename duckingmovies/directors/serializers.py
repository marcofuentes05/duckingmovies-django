from rest_framework import serializers

from directors.models import Director
from awards.serializers import AwardSerializer

class DirectorSerializer(serializers.ModelSerializer):
    awards = AwardSerializer
    class Meta: 
        model = Director
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
