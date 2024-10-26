from django.contrib import admin
from django.urls import path
from mp3_downloader import views

urlpatterns = [
    path('', views.index),
    path('download_audio/', views.download_audio, name='download_audio'),
]
