from django.shortcuts import render, redirect
from .models import Constellation

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def constellations_index(request):
    constellations = Constellation.objects.all()
    return render(request, 'constellations/index.html', {'constellations': constellations })

def constellations_detail(request, constellation_id):
    # DB query
    constellation = Constellation.objects.get(id=constellation_id)
    star_form = StarForm()
    return render(request, 'constellations/detail.html', {
        'constellation': constellation,
        'star_form': star_form
    })