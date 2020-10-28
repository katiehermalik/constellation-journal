from django.db import models

class Constellation:
    def __init__(self, name, symbolism, num_main_stars, brightest_star):
        self.name = name
        self.symbolism = symbolism
        self.num_main_stars = num_main_stars
        self.brightest_star = brightest_star

orion = Constellation('Orion', 'Hunter', 7, 'Rigel')

constellations = [
    Constellation('Corvus', 'Crow', 4, 'γ Crv (Gamma Corvi)'),
    Constellation('Draco', 'Dragon', 14, 'γ Dra (Gamma Draconis)'),
    Constellation('Ursa Minor', 'Little Bear', 7, 'Polaris')
]