from django.db import models
from awards.models import Award
from actors.serializers import ActorSerializer
from directors.serializers import DirectorSerializer
from awards.serializers import AwardSerializer

# Create your models here.
class Serie(models.Model):
    name = models.CharField(max_length=80, null=True)
    rating = models.DecimalField(decimal_places=1, max_digits = 2)
    actors = models.ManyToManyField('actors.actor')
    director = models.ForeignKey(to = 'directors.director', on_delete = models.CASCADE)
    # producer = models.ForeignKey(to = 'producers.producer', on_delete = models.CASCADE)
    seasons = models.IntegerField()
    classification = models.CharField(max_length = 10, null = False)
    comments = models.ManyToManyField('comments.SerieComment') #TODO
    awards = models.ManyToManyField(Award)
    genres = models.ManyToManyField(
        'genres.Genre',
    )
    imageUrl = models.TextField(null=True)
    def __str__(self):
        return 'Serie: {}'.format(self.name)