from pprint import pprint

from django.http import Http404

from stream.models import YouTube
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import GamesServersList, LinkBlog
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .meta import meta_generator


def index(request):
    yt = YouTube.objects.filter(accepted=True).order_by('-id')[:2]
    ptr = LinkBlog.objects.filter(accepted=True).order_by('-id')[:4]
    return render(request, 'service/index.html', {
        'youtube': yt,
        'ptr': ptr,
        'meta': meta_generator()
    })


def livestreams(request):
    meta = {
        'title': 'LiveStream',
        'description': 'Poznaj najlepsze streamy dostępne na platformie Twitch! Tylko od polskich twórców!',
    }
    return render(request, 'player/livestream.html', {
        'meta': meta_generator(meta)
    })


def youtube(request, page=1):
    meta = {
        'title': 'Filmy na YouTube',
        'description': 'Najciekawsze filmy dostępne na YouTube! Zapomnij o "Na czasie" - teraz masz JestemGraczem.pl',
    }

    yt = YouTube.objects.filter(accepted=True).order_by('-id')
    paginator = Paginator(yt, 6)
    youtube_list = paginator.get_page(page)

    return render(request, 'player/youtube.html', {
        'youtube': youtube_list,
        'meta': meta_generator(meta)
    })


def youtube_player(request, videoid):
    yt = get_object_or_404(YouTube, video_id=videoid)
    meta = {
        'title': yt.name,
    }
    return render(request, 'player/youtube_video.html', {
        'youtube': yt,
        'meta': meta_generator(meta)
    })


def gameservers(request):
    official_servers = GamesServersList.objects.filter(official=True)
    servers = GamesServersList.objects.filter(official=False)
    meta = {
        'title': 'Serwery gier',
        'description': 'Profesjonalne serwery gier, TeamSpeak3 i inne! Dla każdego serwery do grania!',
        'keywords': {
            'minecraft',
            'counter-strike',
            'csgo',
            'conan exiles',
            'hurtworld',
            'pubg',
            'server',
            'serwery',
            'za darmo',
            'free'
        }
    }
    return render(request, 'player/gameservers.html', {
        'servers': servers,
        'official_servers': official_servers,
        'meta': meta_generator(meta)
    })


def cooperation(request):
    meta = {
        'title': 'Współpraca'
    }
    return render(request, 'service/cooperation.html', {
        'meta': meta_generator(meta)
    })


def page_not_found(request, exception):
    yt = YouTube.objects.filter(accepted=True).order_by('-id')[:2]
    ptr = LinkBlog.objects.filter(accepted=True).order_by('-id')[:4]
    return render(request, 'service/index.html', {
        'youtube': yt,
        'ptr': ptr,
        'meta': meta_generator()
    }, status=404)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'service/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/website/profile/')
    else:
        form = AuthenticationForm()
    return render(request, 'service/login.html', {'form': form})


@login_required()
def logout_view(request):
    logout(request)
    return render(request, 'service/index.html')
