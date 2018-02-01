from django.urls import path, register_converter
from django.views.decorators.cache import cache_page
from . import views, url_converters

register_converter(url_converters.Username, 'wacek')

urlpatterns = [
    path('mixer/<wacek:username>/', views.mixer, name='stream.mixer'),
    path('twitch/<wacek:username>/', views.twitch, name='stream.twitch'),
    path('live/', cache_page(60 * 1)(views.stream_api), name='stream.live'),
    path('live/esport', cache_page(60 * 10)(views.esport_stream_api), name='stream.live.esport'),
    path('<wacek:username>/', views.streamer, name='stream.streamer'),
    # url(r'^multitwitch/', include([
    #     url(r'^$', views.multitwitch, name="stream.multitwitch"),
    #     url(r'^(?P<username1>[a-zA-Z0-9_]+)/(?P<username2>[a-zA-Z0-9_]+)/$', views.multitwitch,
    #         name='stream.multitwitch.user2'),
    #     url(r'^(?P<username1>[a-zA-Z0-9_]+)/(?P<username2>[a-zA-Z0-9_]+)/(?P<username3>[a-zA-Z0-9_]+)/$',
    #         views.multitwitch,
    #         name='stream.multitwitch.user3'),
    #     url(
    #         r'^(?P<username1>[a-zA-Z0-9_]+)/(?P<username2>[a-zA-Z0-9_]+)/(?P<username3>[a-zA-Z0-9_]+)/'
    #         r'(?P<username4>[a-zA-Z0-9_]+)/$',
    #         views.multitwitch, name='stream.multitwitch.user4')])),
    path('', views.index, name='stream.index'),
]
