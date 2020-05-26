from django.db import models
from awards.models import Award
# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=80,null = False)
    lastName = models.CharField(max_length=80,null = False)
    birthDate = models.DateField()
    birthPlace = models.CharField(max_length=80,null = False)
    netWorth = models.IntegerField()
    height = models.DecimalField(decimal_places = 2, max_digits = 4)
    nickname = models.CharField(max_length = 80, null = True)
    awards = models.ManyToManyField(Award, blank = True)

    def __str__ ( self ) :
        return 'Actor: {} {}'.format(self.name, self.lastName)