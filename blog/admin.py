from django.contrib import admin
from .models import Article, Author

models = Article, Author

admin.site.register(models)
