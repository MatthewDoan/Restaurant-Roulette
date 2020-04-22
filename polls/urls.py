from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.base),
    path('postReq/', views.postReq),
    path('history/', views.history)
]