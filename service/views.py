from stream.models import Mixer, Twitch
from django.shortcuts import render


def index(request):
    mixer = Mixer.objects.all()
    twitch = Twitch.objects.all()
    return render(request, 'service/index.html', {
        'mixer': mixer,
        'twitch': twitch
    })
