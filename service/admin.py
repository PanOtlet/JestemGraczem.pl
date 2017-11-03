from django.contrib import admin
from .models import GamesServersList, AppSettings


@admin.register(GamesServersList)
class GameServersListAdmin(admin.ModelAdmin):
    list_display = ('name', 'official')


@admin.register(AppSettings)
class AppSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
