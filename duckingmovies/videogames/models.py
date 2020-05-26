from django.db import models

# Create your models here.
class Videogame(models.Model):
    title = models.CharField(max_length=200)
    classification = models.CharField(max_length=20)
    release_date = models.DateField()
    developer = models.ForeignKey(
        'developers.Developer',
        on_delete=models.CASCADE,
    )
    genres = models.ManyToManyField(
        'genres.Genre',
    )
    comments = models.ManyToManyField(
        'comments.GameComment',
    )
    rating = models.DecimalField(decimal_places=1, max_digits = 2)
    consoles = models.ManyToManyField(
        'consoles.Console',
    )

    def __str__(self):
        return self.title
