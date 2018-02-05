from stream.models import YouTube
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'service/signup.html', {'form': form})
