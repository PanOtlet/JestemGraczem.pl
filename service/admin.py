from django.contrib import admin
from JestemGraczem.widgets import HtmlEditor
from .models import GamesServersList, AppSettings, LinkBlog


@admin.register(GamesServersList)
class GameServersListAdmin(admin.ModelAdmin):
    list_display = ('name', 'official')


@admin.register(LinkBlog)
class LinkBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'accepted', 'url')


@admin.register(AppSettings)
class AppSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    class Meta:
        fields = 'variable'
        widgets = {
            'code': HtmlEditor(attrs={'style': 'width: 90%; height: 100%;'}),
        }
