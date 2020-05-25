from rest_framework import serializers

from developers.models import Developer

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = (
            'name',
            'country',
            'year_founded',
        )