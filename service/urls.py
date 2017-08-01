from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cooperation/$', views.cooperation, name='service.cooperation'),
    url(r'^$', views.index, name='index'),
]
