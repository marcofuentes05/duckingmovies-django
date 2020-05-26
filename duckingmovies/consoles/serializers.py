from rest_framework import serializers

from consoles.models import Console

class ConsoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Console
        fields = (
            'name',
            'brand',
            'release_date'
        )