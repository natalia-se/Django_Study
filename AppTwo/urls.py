# AppTwo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('profile/', views.profile, name='profile'),  
    path('records/', views.records, name='records'),
]
