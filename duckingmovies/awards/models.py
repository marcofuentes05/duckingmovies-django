from django.db import models

# Create your models here.
class Award(models.Model):
    name = models.CharField(max_length=80, null=False)
    entity = models.CharField(max_length=80, null=False)
    category = models.CharField(max_length=120, null=False)
    year = models.IntegerField()
    
    def __str__(self):
        return str(self.category) + ' in ' + str(self.year)
