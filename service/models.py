from django.db import models


class GamesServersList(models.Model):
    name = models.CharField(max_length=23)
    description = models.TextField()
    official = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Serwery gier'
        verbose_name_plural = 'Serwery gier'

    def __str__(self):
        return 'Serwery: ' + self.name


class AppSettings(models.Model):
    name = models.CharField(max_length=23)
    variable = models.TextField(null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Ustawienia'
        verbose_name_plural = 'Ustawienia'

    def __str__(self):
        return 'Ustawienia: ' + self.name


class LinkBlog(models.Model):
    title = models.CharField('Tytuł', max_length=40)
    url = models.URLField('URL')
    description = models.TextField('Opis', null=True)
    image = models.URLField('Miniatura', null=True)
    accepted = models.BooleanField('Opublikowany', default=False)
    sponsored = models.BooleanField('Artykuł sponsorowany', default=False)
    iframe = models.BooleanField('Ramka', default=True)

    class Meta:
        verbose_name = 'LinkBlog'
        verbose_name_plural = 'LinkBlog'

    def __str__(self):
        return 'LinkBlog: ' + self.title
