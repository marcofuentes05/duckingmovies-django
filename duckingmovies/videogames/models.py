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
        on_delete = models.CASCADE,
    )
    comments = models.ManyToManyField(
        'comments.GameComment',
        on_delete = models.CASCADE,
    )
    rating = models.DecimalField(decimal_places=1)
    consoles = models.ManyToManyField(
        'consoles.Console',
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return str(self)
