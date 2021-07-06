from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home/post_message', views.post_message, name='post_message'),
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
]
