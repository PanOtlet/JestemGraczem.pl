from stream.models import YouTube
from django.shortcuts import render


def index(request):
    youtube = YouTube.objects.order_by('-id')[:20]
    return render(request, 'service/index.html', {
        'youtube': youtube
    })


def cooperation(request):
    return render(request, 'service/cooperation.html')
