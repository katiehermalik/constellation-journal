from django import forms
from .models import Star, Constellation

class StarForm(forms.ModelForm):
  class Meta:
    model = Star
    fields = ('name', 'apparent_magnitude')

class ConstellationForm(forms.ModelForm):
  class Meta:
    model = Constellation
    fields = ('name', 'symbolism', 'num_main_stars', 'brightest_star', 'date_observed')