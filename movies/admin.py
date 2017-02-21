from django.contrib import admin
from .models import Actor, Country, Director, Genre, Movie

models = Actor, Country, Director, Genre, Movie

admin.site.register(models)
