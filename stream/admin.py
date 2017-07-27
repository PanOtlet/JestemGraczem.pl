from django.contrib import admin

from .models import YouTube, Twitch


@admin.register(YouTube)
class YouTubeAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_id')


@admin.register(Twitch)
class TwitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'partner', 'banned')
