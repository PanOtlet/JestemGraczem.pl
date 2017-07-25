from pprint import pprint

from django.shortcuts import redirect, get_object_or_404, render
from config.config import AdminConfig
from service import views
from .models import Mixer, Twitch
from rest_framework import viewsets
from .serializers import TwitchSerializer, MixerSerializer
from twitch import TwitchClient
from django.http import JsonResponse, Http404

# community_id = 'ec04cef0-0e81-4fa9-a037-d11ac87051b6' #Music
community_id = 'ebcc2f09-2677-45f7-8d1f-2442551e6752' #JestemGraczemPL


def twitch_api():
    return TwitchClient(client_id=AdminConfig.TWITCH_API_KEY)


def index(request):
    return redirect(views.index)


def mixer(request, username):
    player = get_object_or_404(Mixer, name=username)
    return render(request, 'player/mixer.html', {'player': player})


def twitch(request, username):
    # player = get_object_or_404(Twitch, name=username)
    twitch_client = twitch_api()
    username2 = twitch_client.users.translate_usernames_to_ids(username)
    community = twitch_client.channels.get_community(username2[0].id)
    pprint(community.id)
    pprint(community_id)
    if community.id == community_id:
        return render(request, 'player/twitch.html', {'player': username})
    raise Http404("Streamer nie jest partnerem JestemGraczem.pl!")


def stream_api(request):
    twitch_client = twitch_api()
    twitch_streams = twitch_client.streams.get_streams_in_community(community_id)
    streams = []
    for stream in twitch_streams:
        pprint(stream.channel.display_name)
        streams.append([
            stream.channel.display_name,
            stream.channel.display_name.lower(),
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
