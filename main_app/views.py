from django.shortcuts import render, redirect
from .models import Constellation, Planet
from .forms import StarForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def constellations_index(request):
    constellations = Constellation.objects.all()
    return render(request, 'constellations/index.html', {'constellations': constellations })

def constellations_detail(request, constellation_id):
    constellation = Constellation.objects.get(id=constellation_id)
    planets_constellation_doesnt_have = Planet.objects.exclude(id__in = constellation.planets.all().values_list('id'))
    star_form = StarForm()
    return render(request, 'constellations/detail.html', {
        'constellation': constellation,
        'star_form': star_form,
        'planets': planets_constellation_doesnt_have
    })

def add_star(request, constellation_id):
  form = StarForm(request.POST)
  if form.is_valid():
    new_star = form.save(commit=False)
    new_star.constellation_id = constellation_id
    new_star.save()
  return redirect('detail', constellation_id=constellation_id)