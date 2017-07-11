from django.shortcuts import redirect
from service import views
from .models import Mixer, Twitch
from django.shortcuts import get_object_or_404, render


def index(request):
    return redirect(views.index)


def mixer(request, username):
    player = get_object_or_404(Mixer, name=username)
    return render(request, 'player/mixer.html', {'player': player})


def twitch(request, username):
    player = get_object_or_404(Twitch, name=username)
    return render(request, 'player/twitch.html', {'player': player})
