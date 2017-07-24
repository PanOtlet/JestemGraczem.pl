from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mixer/(?P<username>[a-zA-Z0-9_]+)/$', views.mixer, name='stream.mixer'),
    url(r'^twitch/(?P<username>[a-zA-Z0-9_]+)/$', views.twitch, name='stream.twitch'),
    url(r'^live/$', views.stream_api, name='stream.live'),
    url(r'^$', views.index, name='stream.index'),
]
