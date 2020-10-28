from django.shortcuts import render, redirect
from .models import Constellation

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def constellations_index(request):
    return render(request, 'constellations/index.html')

