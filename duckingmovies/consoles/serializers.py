from rest_framework import serializers

from consoles.models import Console

class ConsoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Console
        fields = (
            'id',
            'name',
            'brand',
            'release_date'
        )