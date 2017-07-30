from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    url(r'^mixer/(?P<username>[a-zA-Z0-9_]+)/$', views.mixer, name='stream.mixer'),
    url(r'^twitch/(?P<username>[a-zA-Z0-9_]+)/$', views.twitch, name='stream.twitch'),
    url(r'^live/$', cache_page(60 * 10)(views.stream_api), name='stream.live'),
    url(r'^live/esport$', cache_page(60 * 10)(views.esport_stream_api), name='stream.live.esport'),
    url(r'^$', views.index, name='stream.index'),
]
