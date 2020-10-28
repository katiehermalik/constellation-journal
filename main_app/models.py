from django.db import models

class Constellation(models.Model):
    name = models.CharField(max_length=50)
    symbolism = models.TextField(max_length=200)
    num_main_stars = models.IntegerField()
    brightest_star = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Star(models.Model):
    name = models.CharField(max_length=50)
    apparent_magnitude = models.DecimalField(max_digits=2, decimal_places=1)
    date_observed = models.DateField()

    constellation = models.ForeignKey(Constellation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name