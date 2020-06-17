from django.db import models

# Create your models here.

class World_daily(models.Model):
    world_date=models.CharField(max_length=200)
    world_confirmed=models.CharField(max_length=200)
    world_confirmed_change=models.CharField(max_length=200)
    world_death=models.CharField(max_length=200)
    world_death_change=models.CharField(max_length=200)
    world_country=models.CharField(max_length=200)
