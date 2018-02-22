from stream.models import YouTube
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import GamesServersList


def index(request):
    return render(request, 'service/index.html')


def livestreams(request):
    return render(request, 'player/livestream.html')


def youtube(request):
    yt = YouTube.objects.filter(accepted=True).order_by('-id')[:20]
    return render(request, 'player/youtube.html', {
        'youtube': yt
    })


def gameservers(request):
    official_servers = GamesServersList.objects.filter(official=True)
    servers = GamesServersList.objects.filter(official=False)
    return render(request, 'player/gameservers.html', {
        'servers': servers,
        'official_servers': official_servers
    })


def cooperation(request):
    return render(request, 'service/cooperation.html')


def page_not_found(request):
    return render(request, 'service/404.html', status=404)


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
