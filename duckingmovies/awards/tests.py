from django.test import TestCase

# Create your tests here.
class Award(models.Model):
    name = models.CharField(max_length=80,null = False)
    entity = models.CharField(max_length=80,null = False)
    year = models.IntegerField()

    def __str__(self):
        return 'Award: {}'.format(self.name)