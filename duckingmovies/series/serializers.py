from rest_framework import serializers

from series.models import Serie
from actors.serializers import ActorSerializer
from directors.serializers import DirectorSerializer
from awards.serializers import AwardSerializer
from genres.serializers import GenreSerializer
class SerieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer
    director = DirectorSerializer
    awards = AwardSerializer
    genres = GenreSerializer
    class Meta:
        model = Serie
        fields = (
            'id',
            'name',
            'rating',
            'actors',
            'director',
            'seasons',
            'classification',
            'awards',
            'genres',
        )
