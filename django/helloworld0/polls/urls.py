from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls', views.polls, name='polls')
]
