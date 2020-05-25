from django.db import models

# Create your models here.
class Serie(models.Model):
    name = models.CharField(max_length=80, null=True)
    rating = models.DecimalField(decimal_places=1)
    actors = models.ManyToManyField('actors.actor')
    director = models.ForeignKey(to = 'directors.director')
    producer = models.ForeignKey(to = 'producers.producer')
    seasons = models.IntegerField()
    classification = models.CharField(max_length = 10, null = False)
    comments = models.ManyToManyField('comments.comentairo') #TODO

    def __str__(self):
        return 'Serie: {}'.format(self.name)