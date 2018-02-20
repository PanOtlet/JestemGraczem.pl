import random

from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import viewsets
from twitch import TwitchClient

from service import views
from .models import Mixer, Twitch, ESportTwitch
from .serializers import TwitchSerializer, MixerSerializer

from django.conf import settings


def twitch_api():
    return TwitchClient(client_id=settings.TWITCH_API_KEY)


def index(request):
    return redirect(views.index)


def stream_api(request):
    twitch_client = twitch_api()
    twitch_players = Twitch.objects.all().filter(banned=False)

    twitch_players_ids = ''
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

    if len(partner_stream) < 1:
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
