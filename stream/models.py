from django.db import models
from django.contrib.auth.models import User


class Twitch(models.Model):
    name = models.CharField('Nazwa', max_length=23)
    twitch_id = models.IntegerField('Twitch ID', null=True)
    add_date = models.DateTimeField('Data publikacji')
    partner = models.BooleanField('Partner', default=False)
    banned = models.BooleanField('Blokada', default=False)
    accepted = models.BooleanField('Opublikowany', default=False)
    youtube_url = models.URLField('Kanał YouTube', null=True, blank=True)
    facebook_url = models.URLField('Facebook', null=True, blank=True)

    class Meta:
        verbose_name = 'Kanały Twitch.tv'
        verbose_name_plural = 'Kanały Twitch.tv'

    def __str__(self):
        return 'Twitch: ' + self.name


class YouTube(models.Model):
    name = models.CharField('Nazwa', max_length=50)
    add_date = models.DateTimeField('Data publikacji')
    video_id = models.CharField('ID Wideo', max_length=23)
    accepted = models.BooleanField('Opublikowany', default=False)

    class Meta:
        verbose_name = 'Filmy na YouTube'
        verbose_name_plural = 'Filmy na YouTube'

    def __str__(self):
        return 'YouTube: ' + self.name


class ESportTwitch(models.Model):
    name = models.CharField('Nazwa kanału', max_length=23)
    twitch_id = models.IntegerField('Twitch ID')

    class Meta:
        verbose_name = 'Kanały eSport Twitch'
        verbose_name_plural = 'Kanały eSport Twitch'

    def __str__(self):
        return 'eSport Twitch: ' + self.name
