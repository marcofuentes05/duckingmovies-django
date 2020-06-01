from rest_framework import serializers

from comments.models import GameComment, MovieComment, SerieComment
#TODO import serializer user
from django.contrib.auth.models import User
from usuarios.serializers import UserSerializer

class GameCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer
    class Meta:
        model = GameComment
        fields = (
            'id',
            'author',
            'text'
        )

class MovieCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer
    class Meta:
        model = MovieComment
        fields = (
            'id',
            'author',
            'text'
        )

class SerieCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer
    class Meta:
        model = SerieComment
        fields = (
            'id',
            'author',
            'text'
        )