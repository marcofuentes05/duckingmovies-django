from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'name',
            'rating',
            'actors',
            'director',
            'budget',
            'duration',
            'classification',
            'award'
        )
