# from django.contrib import admin
from django.urls import path
from embed_editor import views

urlpatterns = [
    path('', views.index),
]
