# Generated by Django 3.0.4 on 2020-06-01 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='imageUrl',
            field=models.TextField(null=True),
        ),
    ]
