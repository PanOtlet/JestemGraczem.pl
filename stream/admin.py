from django.contrib import admin

from .models import Twitch, Mixer

admin.site.register(Twitch)
admin.site.register(Mixer)
