from rest_framework import serializers

from videogames.models import Videogame
from developers.serializers import DeveloperSerializer
from genres.serializers import GenreSerializer
from comments.serializers import GameCommentSerializer
from consoles.serializers import ConsoleSerializer



class VideogameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer
    developer = DeveloperSerializer
    comments = GameCommentSerializer
    consoles = ConsoleSerializer
    class Meta:
        model = Videogame
        fields = (
            'id',
            'title',
            'rating',
            'classification',
            'release_date',
            'developer',
            'genres',
            'comments',
            'consoles',
        )