from rest_framework import serializers

from movie_producers.models import MovieProducer



class MovieProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieProducer
        fields = (
            'name',
            'country',
            'year_founded',
        )