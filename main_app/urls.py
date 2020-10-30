from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('constellations/', views.constellations_index, name='constellations_index'),
    path('constellations/new/', views.add_constellation, name='add_constellation'),
    path('constellations/<int:constellation_id>/', views.constellations_detail, name='detail'),
    path('constellations/<int:constellation_id>/add_star/', views.add_star, name='add_star'),
    path('constellations/<int:constellation_id>/assoc_planet/<int:planet_id>/', views.assoc_planet, name='assoc_planet'),
    path('constellations/<int:constellation_id>/dissociate_planet/<int:planet_id>/', views.dissociate_planet, name='dissociate_planet'),
]

