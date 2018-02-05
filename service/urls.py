from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/',  auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    path('cooperation/', views.cooperation, name='service.cooperation'),
    path('', cache_page(60 * 1)(views.index), name='index'),
]
