from django.db import models
from django.contrib.auth.models import User


class Twitch(models.Model):
    name = models.CharField(max_length=23)
    add_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User)
    partner = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)


class Mixer(models.Model):
    name = models.CharField(max_length=23)
    add_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User)
    partner = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)


class YouTube(models.Model):
    name = models.CharField(max_length=50)
    add_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User)
    video_id = models.CharField(max_length=23)

    class Meta:
        verbose_name = 'Filmy na YouTube'
        verbose_name_plural = 'Filmy na YouTube'
