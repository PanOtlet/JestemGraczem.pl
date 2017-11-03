from django.db import models


class GamesServersList(models.Model):
    name = models.CharField(max_length=23)
    description = models.TextField()
    official = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Serwery gier'
        verbose_name_plural = 'Serwery gier'


class AppSettings(models.Model):
    name = models.CharField(max_length=23)
    variable = models.TextField(null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Ustawienia'
        verbose_name_plural = 'Ustawienia'
