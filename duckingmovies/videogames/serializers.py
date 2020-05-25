from rest_framework import serializers

from videogames.models import Videogame
from developers.serializers import DeveloperSerializer
# TODO import de serializer genero
from comments.serializers import GameCommentSerializer
from consoles.serializers import ConsoleSerializer



class VideogameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = (
            'title',
            'rating',
            'classification',
            'release_date',
            'developer',
            'genres',
            'comments',
            'consoles',
        )