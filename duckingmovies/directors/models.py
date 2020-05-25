from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=80,null = False)
    lastName = models.CharField(max_length=80,null = False)
    birthDate = models.DateField()
    birthPlace = models.CharField(max_length=80,null = False)
    netWorth = models.IntegerField()
    height = models.DecimalField()
    nickname = models.CharField(max_length = 80, null = True)
    awards = models.ManyToManyField('awards.award')

    def __str__(self):
        return 'Director: {}'.format(self.name)