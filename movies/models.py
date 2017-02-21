from django.db import models


class Human(models.Model):
    firstname = models.CharField('Имечко', max_length=30)
    lastname = models.CharField('Фамилия', max_length=30)
    birthdate = models.DateField('Дата рождения', blank=True, null=True)
    photo = models.ImageField('Фото', upload_to='photos', blank=True, null=True)

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        return self.get_full_name()

    class Meta:
        abstract = True


class Director(Human):
    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Actor(Human):
    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Country(models.Model):
    name = models.CharField('Страна', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField('Название', max_length=255)
    poster = models.ImageField('Постер', upload_to='movie/poster')
    created = models.DateField('Год', blank=True, null=True)
    countries = models.ManyToManyField(Country, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    premiere = models.DateField('Дата премьеры', blank=True, null=True)
    duration = models.SmallIntegerField('Продолжительность', help_text='в минутах', blank=True, null=True)

    def __str__(self):
        if self.created:
            return f'{self.title} ({self.created.year})'
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
