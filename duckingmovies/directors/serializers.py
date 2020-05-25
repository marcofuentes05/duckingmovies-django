from rest_framework import serializers

from directors.models import Director
from awards.models import Award

class DirectorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Director
        fields = (
            'name',
            'lastName',
            'birthDate',
            'birthPlace',
            'netWorth',
            'height',
            'nickname',
            'awards'
        )
