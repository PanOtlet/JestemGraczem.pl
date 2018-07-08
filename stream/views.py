import json
import random
import requests

from JestemGraczem.settings import TWITCH_API_KEY

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.datetime_safe import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework import viewsets
from twitch import TwitchClient

from service import views
from .forms import YouTubeForm, TwitchForm
from .models import Twitch, ESportTwitch, YouTube
from .serializers import TwitchSerializer

from django.conf import settings


def twitch_api():
    return TwitchClient(client_id=settings.TWITCH_API_KEY)


def index(request):
    return redirect(views.index)


def add_youtube(request):
    if request.method == 'POST':
        form = YouTubeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            video_id = form.cleaned_data['video_id']
            try:
                YouTube.objects.get(video_id=video_id)
                return render(request, 'service/youtube_form.html', {
                    'form': form,
                    'info': [
                        'red',
                        'Podany film już jest w naszej bazie!'
                    ]
                })
            except ObjectDoesNotExist:
                YouTube.objects.create(name=name, video_id=video_id, add_date=datetime.now(), accepted=False)
                send_mail(
                    'Nowy film',
                    'Dodano nowy film do bazy danych',
                    'admin@jestemgraczem.pl',
                    ['otlet@otlet.pl'],
                    fail_silently=False,
                )
                return render(request, 'service/youtube_form.html', {
                    'form': form,
                    'info': [
                        'green',
                        'Film został dodany! Oczekuje na akceptację'
                    ]
                })
    else:
        form = YouTubeForm()
    return render(request, 'service/youtube_form.html', {'form': form})


def add_twitch(request):
    if request.method == 'POST':
        form = TwitchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                Twitch.objects.get(name=username)
                return render(request, 'service/twitch_form.html', {
                    'form': form,
                    'info': [
                        'red',
                        'Streamer już jest w naszej bazie!'
                    ]
                })
            except ObjectDoesNotExist:
                url = 'https://api.twitch.tv/kraken/users?login=' + username
                headers = {
                    'Accept': 'application/vnd.twitchtv.v5+json',
                    'Client-ID': TWITCH_API_KEY
                }
                r = requests.get(url, headers=headers)
                load = json.loads(r.text)
                if load['_total'] == 1:
                    Twitch.objects.create(name=load['users'][0]['name'], twitch_id=load['users'][0]['_id'],
                                          add_date=datetime.now(), accepted=False)
                    send_mail(
                        'Nowy streamer w bazie',
                        'Ktoś właśnie dodał nowy stream w bazie!',
                        'admin@jestemgraczem.pl',
                        ['otlet@otlet.pl'],
                        fail_silently=False,
                    )
                    return render(request, 'service/twitch_form.html', {
                        'form': form,
                        'info': [
                            'green',
                            'Streamer został dodany! Oczekuje na akceptację'
                        ]
                    })
                elif load['_total'] == 0:
                    return render(request, 'service/twitch_form.html', {
                        'form': form,
                        'info': [
                            'red',
                            'Taki streamer nie istnieje!'
                        ]
                    })
                return render(request, 'service/twitch_form.html', {
                    'form': form,
                    'info': [
                        'red',
                        'Panie, ale mnie tutaj bez przecinków dawaj!'
                    ]
                })
    else:
        form = TwitchForm()
    return render(request, 'service/twitch_form.html', {'form': form})


def stream_api(request):
    twitch_client = twitch_api()
    twitch_players = Twitch.objects.all().filter(banned=False, accepted=True)

    twitch_players_ids = ''
    for player in twitch_players:
        twitch_players_ids += str(player.twitch_id) + ','

    streams = partner_stream = []

    if not twitch_players_ids is '':
        twitch_streams = twitch_client.streams.get_live_streams(twitch_players_ids)

    for stream in twitch_streams:
        partner_stream.append([
            stream.channel.display_name,
            stream.channel.display_name.lower(),
            stream.game,
            stream.preview["large"],
            stream.id,
            stream.viewers,
            stream.channel.description
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
                stream.id,
                stream.viewers,
                stream.channel.description
            ])

    return JsonResponse(streams, safe=False)


def esport_stream_api(request):
    twitch_client = twitch_api()
    twitch_players = ESportTwitch.objects.all()
    twitch_players_ids = ''
    for player in twitch_players:
        twitch_players_ids += str(player.twitch_id) + ','
    streams = []
    if not twitch_players_ids is '':
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
