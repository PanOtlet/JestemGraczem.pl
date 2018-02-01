import os
import random

from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from rest_framework import viewsets
from twitch import TwitchClient

from service import views
from .models import Mixer, Twitch, ESportTwitch
from .serializers import TwitchSerializer, MixerSerializer

if 'TRAVIS' in os.environ:
    from config.travis import AdminConfig
else:
    from config.config import AdminConfig


def twitch_api():
    return TwitchClient(client_id=AdminConfig.TWITCH_API_KEY)


def index(request):
    return redirect(views.index)


def streamer(request, username):
    player = [get_object_or_404(Twitch, name=username)]
    twitch_client = twitch_api()
    player.append(twitch_client.channels.get_by_id(player[0].twitch_id))
    return render(request, 'player/partner_page.html', {
        'player': player
    })


def mixer(request, username):
    player = get_object_or_404(Mixer, name=username)
    return render(request, 'player/mixer.html', {'player': player})


def twitch(request, username):
    try:
        player = Twitch.objects.get(name__icontains=username)
    except Twitch.DoesNotExist:
        return render(request, 'player/twitch.html', {'player': username})
    if player.partner is True:
        return redirect('stream.streamer', username=player.name)

    return render(request, 'player/twitch.html', {'player': username})


def stream_api(request):
    twitch_client = twitch_api()
    twitch_players = Twitch.objects.all().filter(banned=False)

    twitch_players_ids = 'jestemgraczemtv,'
    for player in twitch_players:
        twitch_players_ids += str(player.twitch_id) + ','

    streams = partner_stream = []

    twitch_streams = twitch_client.streams.get_live_streams(twitch_players_ids)

    for stream in twitch_streams:
        partner_stream.append([
            stream.channel.display_name,
            stream.channel.display_name.lower(),
            stream.game,
            stream.preview["large"],
            stream.id,
            True
        ])

    twitch_random_streams = twitch_client.streams.get_live_streams(language='pl', limit=100)
    random.shuffle(twitch_random_streams)
    twitch_streams = twitch_streams + twitch_random_streams

    for stream in twitch_streams:
        streams.append([
            stream.channel.display_name,
            stream.channel.display_name.lower(),
            stream.game,
            stream.preview["large"],
            stream.id
        ])

    return JsonResponse(streams, safe=False)


def esport_stream_api(request):
    twitch_client = twitch_api()
    twitch_players = ESportTwitch.objects.all()
    twitch_players_ids = ''
    for player in twitch_players:
        twitch_players_ids += str(player.twitch_id) + ','
    streams = []
    twitch_streams = twitch_client.streams.get_live_streams(twitch_players_ids)
    for stream in twitch_streams:
        streams.append([
            stream.channel.display_name,
            stream.channel.display_name.lower(),
            stream.game,
            stream.preview["large"],
            stream.id
        ])
    return JsonResponse(streams, safe=False)


class TwitchViewSet(viewsets.ModelViewSet):
    queryset = Twitch.objects.all().order_by('-partner')
    serializer_class = TwitchSerializer


class MixerViewSet(viewsets.ModelViewSet):
    queryset = Mixer.objects.all().order_by('-partner')
    serializer_class = MixerSerializer
