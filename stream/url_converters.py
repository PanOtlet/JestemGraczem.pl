# path('mixer/(?P<username>v+)/', views.mixer, name='stream.mixer'),
#     path('twitch/(?P<username>[a-zA-Z0-9_]+)/', views.twitch, name='stream.twitch'),
#     path('live/', cache_page(60 * 1)(views.stream_api), name='stream.live'),
#     path('live/esport', cache_page(60 * 10)(views.esport_stream_api), name='stream.live.esport'),
#     path('(?P<username>[a-zA-Z0-9_]+)/', views.streamer, name='stream.s


class Username:
    regex = '[a-zA-Z0-9_]'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
