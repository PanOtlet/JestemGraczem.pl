from django.db import models


class GamesServersList(models.Model):
    name = models.CharField(max_length=23)
    description = models.TextField()
    official = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Serwery gier'
        verbose_name_plural = 'Serwery gier'
