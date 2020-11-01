from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Constellation, Planet
from .forms import StarForm, ConstellationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# --------------------------------------- STATIC PAGES
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# --------------------------------------- CONSTELLATIONS
def constellations_index(request):
    constellations = Constellation.objects.filter(user=request.user)
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

def add_constellation(request):
    if request.method == 'POST':
        constellation_form = ConstellationForm(request.POST)
        if constellation_form.is_valid():
            new_constellation = constellation_form.save(commit=False)
            new_constellation.user = request.user
            new_constellation.save()
            return redirect('detail', new_constellation.id)
    else: 
        form = ConstellationForm()
        context = {'form': form}
        return render(request, 'constellations/new.html', context)


def edit_constellation(request, constellation_id):
    constellation = Constellation.objects.get(id=constellation_id)
    if request.method == 'POST':
        constellation_form = ConstellationForm(request.POST, instance=constellation)
        if constellation_form.is_valid():
            updated_constellation = constellation_form.save()
            return redirect('detail', updated_constellation.id)
    else: 
        form = ConstellationForm(instance=constellation)
        context = {'form': form}
        return render(request, 'constellations/edit.html', context)


def delete_constellation(request, constellation_id):
    Constellation.objects.get(id=constellation_id).delete()
    return redirect('constellations_index')


# --------------------------------------- CONSTELLATION STARS
def add_star(request, constellation_id):
    form = StarForm(request.POST)
    if form.is_valid():
        new_star = form.save(commit=False)
        new_star.constellation_id = constellation_id
        new_star.save()
    return redirect('detail', constellation_id=constellation_id)


# --------------------------------------- CONSTELLATION PLANETS
def assoc_planet(request, constellation_id, planet_id):
    planet = Planet.objects.get(id=planet_id)
    Constellation.objects.get(id=constellation_id).planets.add(planet)
    return redirect('detail', constellation_id)


def dissociate_planet(request, constellation_id, planet_id):
    planet = Planet.objects.get(id=planet_id)
    Constellation.objects.get(id=constellation_id).planets.remove(planet)
    return redirect('detail', constellation_id)


# --------------------------------------- AUTH
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('constellations_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)