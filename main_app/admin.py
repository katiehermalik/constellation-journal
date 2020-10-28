from django.contrib import admin
from .models import Constellation, Star, Planet

admin.site.register(Constellation)
admin.site.register(Star)
admin.site.register(Planet)