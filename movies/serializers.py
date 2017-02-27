from rest_framework import serializers

from .models import Actor, Country, Director, Genre, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        # указываем какую модель сериализовывать
        model = Actor
        # указываем какие поля модели сериализовывать
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
