from django.conf.urls import url, include
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    url(r'^mixer/(?P<username>[a-zA-Z0-9_]+)/$', views.mixer, name='stream.mixer'),
    url(r'^twitch/(?P<username>[a-zA-Z0-9_]+)/$', views.twitch, name='stream.twitch'),
    url(r'^multitwitch/', include([
        url(r'^$', views.multitwitch, name="stream.multitwitch"),
        url(r'^(?P<username1>[a-zA-Z0-9_]+)/(?P<username2>[a-zA-Z0-9_]+)/$', views.multitwitch,
            name='stream.multitwitch.user2'),
        url(r'^(?P<username1>[a-zA-Z0-9_]+)/(?P<username2>[a-zA-Z0-9_]+)/(?P<username3>[a-zA-Z0-9_]+)/$',
            views.multitwitch,
            name='stream.multitwitch.user3'),
        url(
            r'^(?P<username1>[a-zA-Z0-9_]+)/(?P<username2>[a-zA-Z0-9_]+)/(?P<username3>[a-zA-Z0-9_]+)/'
            r'(?P<username4>[a-zA-Z0-9_]+)/$',
            views.multitwitch, name='stream.multitwitch.user4')])),
    url(r'^live/$', cache_page(60 * 10)(views.stream_api), name='stream.live'),
    url(r'^live/esport$', cache_page(60 * 10)(views.esport_stream_api), name='stream.live.esport'),
    url(r'^(?P<username>[a-zA-Z0-9_]+)/$', views.streamer, name='stream.streamer'),
    url(r'^$', views.index, name='stream.index'),
]
