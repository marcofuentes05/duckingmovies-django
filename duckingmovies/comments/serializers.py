from rest_framework import serializers

from comments.models import GameComment, MovieComment, SerieComment
#TODO import serializer user
from django.contrib.auth.models import User

class GameCommentSerializer(serializers.ModelSerializer):
    author = #serializer user
    class Meta:
        model = GameComment
        fields = (
            'author',
            'text'
        )

class MovieCommentSerializer(serializers.ModelSerializer):
    author = #serializer user
    class Meta:
        model = MovieComment
        fields = (
            'author',
            'text'
        )

class SerieCommentSerializer(serializers.ModelSerializer):
    author = #serializer user
    class Meta:
        model = SerieComment
        fields = (
            'author',
            'text'
        )