# Generated by Django 3.0.4 on 2020-05-25 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_award_category'),
        ('movies', '0002_auto_20200525_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='award',
            field=models.ManyToManyField(to='awards.Award'),
        ),
    ]
