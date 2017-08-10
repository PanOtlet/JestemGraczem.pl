from django.db import models
from django.contrib.auth.models import User


class Twitch(models.Model):
    name = models.CharField(max_length=23)
    twitch_id = models.IntegerField(null=True)
    add_date = models.DateTimeField('date published')
    partner = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)
    youtube_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Kanały Twitch.tv'
        verbose_name_plural = 'Kanały Twitch.tv'


class Mixer(models.Model):
    name = models.CharField(max_length=23)
    add_date = models.DateTimeField('date published')
    partner = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)


class YouTube(models.Model):
    name = models.CharField(max_length=50)
    add_date = models.DateTimeField('date published')
    video_id = models.CharField(max_length=23)

    class Meta:
        verbose_name = 'Filmy na YouTube'
        verbose_name_plural = 'Filmy na YouTube'


class ESportTwitch(models.Model):
    name = models.CharField(max_length=23)
    twitch_id = models.IntegerField()

    class Meta:
        verbose_name = 'Kanały eSport Twitch'
        verbose_name_plural = 'Kanały eSport Twitch'
