# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, verbose_name='Имечко')),
                ('lastname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, verbose_name='Имечко')),
                ('lastname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('poster', models.ImageField(upload_to='movie/poster', verbose_name='Постер')),
                ('created', models.DateField(blank=True, null=True, verbose_name='Год')),
                ('premiere', models.DateField(blank=True, null=True, verbose_name='Дата премьеры')),
                ('duration', models.SmallIntegerField(blank=True, help_text='в минутах', null=True, verbose_name='Продолжительность')),
                ('actors', models.ManyToManyField(blank=True, to='movies.Actor')),
                ('countries', models.ManyToManyField(blank=True, to='movies.Country')),
                ('directors', models.ManyToManyField(blank=True, to='movies.Director')),
                ('genres', models.ManyToManyField(blank=True, to='movies.Genre')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
