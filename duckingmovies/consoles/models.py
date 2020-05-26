from django.db import models

# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name