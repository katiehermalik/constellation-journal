# Generated by Django 3.1.2 on 2020-10-30 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_constellation_planets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='date_observed',
        ),
    ]