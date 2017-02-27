from rest_framework import viewsets

from .models import Actor, Country, Director, Genre, Movie
from .serializers import ActorSerializer, CountrySerializer, DirectorSerializer, GenreSerializer, MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    # какие данные использовать
    # в данном случае все записи из модели Actor
    queryset = Actor.objects.all()
    # какой сериализатор использовать
    serializer_class = ActorSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
