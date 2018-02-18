from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('signup/', views.registration, name='signup'),
    path('login/', views.login_view, name='login'),
    path('cooperation/', views.cooperation, name='service.cooperation'),
    path('livestreams/', cache_page(60 * 1)(views.livestreams), name='livestreams'),
    path('youtube/', cache_page(60 * 1)(views.youtube), name='youtube'),
    path('gameservers/', cache_page(60 * 1)(views.gameservers), name='gameservers'),
    path('', cache_page(60 * 1)(views.index), name='index'),
]
