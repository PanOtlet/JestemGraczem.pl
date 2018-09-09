from django.contrib import admin

from JestemGraczem.widgets import HtmlEditor
from .models import GamesServersList, AppSettings, LinkBlog, RSS


@admin.register(GamesServersList)
class GameServersListAdmin(admin.ModelAdmin):
    list_display = ('name', 'official')


@admin.register(LinkBlog)
class LinkBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'accepted', 'partner', 'sponsored', 'url')


@admin.register(RSS)
class RSSAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


@admin.register(AppSettings)
class AppSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    class Meta:
        fields = 'variable'
        widgets = {
            'code': HtmlEditor(attrs={'style': 'width: 90%; height: 100%;'}),
        }
