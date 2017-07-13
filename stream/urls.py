from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mixer/(?P<username>[a-zA-Z0-9_]+)/$', views.mixer, name='stream.mixer'),
    url(r'^twitch/', views.twitch_detail),
    url(r'^twitch/(?P<username>[a-zA-Z0-9_]+)/$', views.twitch, name='stream.twitch'),
    url(r'^$', views.index, name='stream.index'),
]
