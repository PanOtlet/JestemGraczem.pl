from django.contrib import admin

from .models import YouTube, Twitch, ESportTwitch


@admin.register(YouTube)
class YouTubeAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_id')


@admin.register(Twitch)
class TwitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'partner', 'banned', 'twitch_id')


@admin.register(ESportTwitch)
class ESportTwitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'twitch_id')
