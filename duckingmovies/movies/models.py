from django.db import models
from awards.models import Award
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=80, null=True)
    rating = models.DecimalField(decimal_places=1, max_digits = 4 )
    actors = models.ManyToManyField('actors.actor')
    director = models.ForeignKey(to = 'directors.director', on_delete = models.CASCADE)
    producer = models.ForeignKey(to = 'movie_producers.MovieProducer', on_delete = models.CASCADE, default = 1)
    budget = models.DecimalField(decimal_places=2, max_digits = 4)
    duration = models.DecimalField(decimal_places=2, max_digits = 5)
    classification = models.CharField(max_length = 10, null = False)
    award = models.ManyToManyField(Award)
    comments = models.ManyToManyField('comments.MovieComment') #TODO
    
    # Movie(name = 'test movie',rating =  4.5 , budget = 90.0, duration = 90.5, classification = 'A')
    def __str__(self):
        return 'Movie: {}'.format(self.name)