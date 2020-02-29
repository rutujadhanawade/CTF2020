from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign', views.signup, name='signup'),
    path('login',views.login,name='login'),
    path('ctf/first.html',views.first,name='first')
]
