from django.contrib import admin

from .models import Actor, Country, Director, Genre, Movie

# регистрируем наши модели в автоадминке
# чтобы можно было работать с базой через нее

models = Actor, Country, Director, Genre, Movie

admin.site.register(models)
