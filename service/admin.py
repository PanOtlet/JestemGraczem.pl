from django.contrib import admin
from .models import GamesServersList


@admin.register(GamesServersList)
class GameServersListAdmin(admin.ModelAdmin):
    list_display = ('name', 'official')
