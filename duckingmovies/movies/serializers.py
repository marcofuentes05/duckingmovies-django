from rest_framework import serializers

from movies.models import Movie
from actors.serializers import ActorSerializer
from directors.serializers import DirectorSerializer
from awards.serializers import AwardSerializer
from comments.serializers import MovieCommentSerializer

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer
    director = DirectorSerializer
    award = AwardSerializer
    comments = MovieCommentSerializer
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
            'award',
            'comments'
        )
