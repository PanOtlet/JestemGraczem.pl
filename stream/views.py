from django.shortcuts import redirect
from service import views
from .models import Mixer, Twitch
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TwitchSerializer


def index(request):
    return redirect(views.index)


def mixer(request, username):
    player = get_object_or_404(Mixer, name=username)
    return render(request, 'player/mixer.html', {'player': player})


def twitch(request, username):
    player = get_object_or_404(Twitch, name=username)
    return render(request, 'player/twitch.html', {'player': player})


@api_view(['GET'])
def twitch_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        twitchobj = Twitch.objects.get(pk=pk)
    except Twitch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TwitchSerializer(twitchobj)
        return Response(serializer.data)
