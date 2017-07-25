from django.contrib import admin

from .models import YouTube


@admin.register(YouTube)
class YouTubeAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_id')
