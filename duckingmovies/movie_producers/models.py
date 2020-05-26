from django.db import models

# Create your models here.
class MovieProducer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    year_founded = models.IntegerField()

    def __str__(self):
        return self.name