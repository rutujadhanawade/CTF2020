from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('login', views.login1, name='login1'),
    path('instructions', views.inst, name='inst'),
    path('QUEST', views.Quest, name='Quest'),
    path('logout', views.logout, name='logout'),
    path('check', views.check, name='check'),
    path('hint', views.hint, name='hint'),
    path('leaderboard', views.leaderboard, name='leaderboard')
]
