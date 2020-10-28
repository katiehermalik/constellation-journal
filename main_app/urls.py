from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('constellations/', views.constellations_index, name='index'),
    path('constellations/<int:constellation_id>/', views.constellations_detail, name='detail'),
    path('cats/<int:constellation_id>/add_star/', views.add_star, name='add_star')
]

