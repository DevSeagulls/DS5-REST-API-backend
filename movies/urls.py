from django.conf.urls import url, include
from rest_framework import routers

from .views import ActorViewSet, CountryViewSet, DirectorViewSet, GenreViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'actors', ActorViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'movies', MovieViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
