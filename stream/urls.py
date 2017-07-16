from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'twitch', views.TwitchViewSet)
router.register(r'mixer', views.MixerViewSet)

urlpatterns = [
    url(r'^mixer/(?P<username>[a-zA-Z0-9_]+)/$', views.mixer, name='stream.mixer'),
    url(r'^twitch/(?P<username>[a-zA-Z0-9_]+)/$', views.twitch, name='stream.twitch'),
    url(r'^api/', include(router.urls, namespace='stream.api')),
    url(r'^$', views.index, name='stream.index'),
]
