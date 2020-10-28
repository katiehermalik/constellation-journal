# Generated by Django 3.1.2 on 2020-10-28 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('apparent_magnitude', models.DecimalField(decimal_places=1, max_digits=2)),
                ('date_observed', models.DateField()),
                ('constellation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.constellation')),
            ],
        ),
    ]
