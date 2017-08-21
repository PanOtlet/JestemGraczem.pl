from stream.models import YouTube
from django.shortcuts import render
from .models import GamesServersList


def index(request):
    youtube = YouTube.objects.order_by('-id')[:20]
    official_servers = GamesServersList.objects.filter(official=True)
    servers = GamesServersList.objects.filter(official=False)
    return render(request, 'service/index.html', {
        'youtube': youtube,
        'servers': servers,
        'official_servers': official_servers
    })


def cooperation(request):
    return render(request, 'service/cooperation.html')


def page_not_found(request):
    return render(request, 'service/404.html', status=404)
