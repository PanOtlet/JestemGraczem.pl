from django.shortcuts import redirect, get_object_or_404, render
from config.config import AdminConfig
from service import views
from .models import Mixer, Twitch
from rest_framework import viewsets
from .serializers import TwitchSerializer, MixerSerializer
from twitch import TwitchClient
from django.http import JsonResponse


def index(request):
    return redirect(views.index)


def mixer(request, username):
    player = get_object_or_404(Mixer, name=username)
    return render(request, 'player/mixer.html', {'player': player})


def twitch(request, username):
    player = get_object_or_404(Twitch, name=username)
    return render(request, 'player/twitch.html', {'player': player})


def stream_api(request):
    twitch_client = TwitchClient(client_id=AdminConfig.TWITCH_API_KEY)
    twitch_streams = twitch_client.streams.get_streams_in_community('ebcc2f09-2677-45f7-8d1f-2442551e6752')
    # twitch_streams = twitch_client.streams.get_streams_in_community('ad14d4fc-1a7c-413f-aa32-4906ef3669ae')
    streams = []
    for stream in twitch_streams:
        streams.append([
            stream.channel.display_name,
            stream.game,
            stream.preview["large"]
        ])
    return JsonResponse(streams, safe=False)


class TwitchViewSet(viewsets.ModelViewSet):
    queryset = Twitch.objects.all().order_by('-partner')
    serializer_class = TwitchSerializer


class MixerViewSet(viewsets.ModelViewSet):
    queryset = Mixer.objects.all().order_by('-partner')
    serializer_class = MixerSerializer
