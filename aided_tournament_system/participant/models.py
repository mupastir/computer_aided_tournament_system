import uuid as uuid_lib
from enum import Enum

from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from user_auth.models import User


class Player(User):
    class SEXES(Enum):
        woman = ('w', 'Woman')
        man = ('m', 'Man')

    slug = models.SlugField(unique=True, verbose_name='slug')
    sex = models.CharField(
        max_length=1,
        choices=[x.value for x in SEXES],
        verbose_name='sex'
    )

    country = CountryField(
        blank_label='(select country)',
        verbose_name='sex'
    )
    rating = models.IntegerField(
        null=True,
        verbose_name='rating'
    )

    def get_absolute_url(self):
        return reverse('flavors:detail', kwargs={'slug': self.slug})


class Team(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False,
        primary_key=True
    )
    slug = models.SlugField(unique=True, verbose_name='slug')
    title = models.CharField(
        max_length=100
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        verbose_name='players'
    )
    rating = models.IntegerField(
        null=True,
        verbose_name='total team rating'
    )

    def get_absolute_url(self):
        return reverse('flavors:detail', kwargs={'slug': self.slug})


class Referee(User):
    pass


class ScoreMarker(User):
    pass
