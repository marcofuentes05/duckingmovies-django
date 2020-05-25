# Generated by Django 3.0.4 on 2020-05-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('lastName', models.CharField(max_length=80)),
                ('birthDate', models.DateField()),
                ('birthPlace', models.CharField(max_length=80)),
                ('netWorth', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('nickname', models.CharField(max_length=80, null=True)),
                ('awards', models.ManyToManyField(to='awards.Award')),
            ],
        ),
    ]