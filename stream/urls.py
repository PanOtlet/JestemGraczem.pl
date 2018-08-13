from django.urls import path, register_converter
from django.views.decorators.cache import cache_page
from . import views, url_converters

register_converter(url_converters.Username, 'wacek')

urlpatterns = [
    path('live/', cache_page(60 * 1)(views.stream_api), name='stream.live'),
    path('live/esport', cache_page(60 * 10)(views.esport_stream_api), name='stream.live.esport'),
    path('live/partners', cache_page(60 * 10)(views.partner_stream_api), name='stream.live.partner'),
    path('add/youtube/', views.add_youtube, name='add.youtube'),
    path('add/twitch/', views.add_twitch, name='add.twitch'),
    # path('', views.index, name='stream.index'),
]
