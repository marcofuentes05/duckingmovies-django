from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin (models.Model):
    idu = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE, null = False)
    def __str__(self):
        return 'Admin: {}'.format(self.idu)