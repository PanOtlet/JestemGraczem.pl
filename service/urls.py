from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cooperation/', views.cooperation, name='service.cooperation'),
    path('', cache_page(60 * 1)(views.index), name='index'),
]
