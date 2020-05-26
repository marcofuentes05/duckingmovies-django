from rest_framework import serializers

from movies.models import Movie
from actors.serializers import ActorSerializer
from directors.serializers import DirectorSerializer
from awards.serializers import AwardSerializer

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer
    director = DirectorSerializer
    award = AwardSerializer
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
