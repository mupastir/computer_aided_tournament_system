from enum import Enum

from competition.models import Application
from django.db import models
from django_countries.fields import CountryField
from django_utils.models import UUIDTimeStampModel
from game.models import Game


class Player(UUIDTimeStampModel):
    class GENDER(Enum):
        woman = ('w', 'Woman')
        man = ('m', 'Man')

    user = models.UUIDField(verbose_name='users uuid', unique=True)
    gender = models.CharField(max_length=1,
                              choices=[x.value for x in GENDER],
                              verbose_name='sex')
    country = CountryField(blank_label='(select country)',
                           verbose_name='country')
    rating = models.IntegerField(null=True,
                                 verbose_name='rating')
    team = models.ManyToManyField('Team',
                                  blank=True,
                                  verbose_name='team')


class Team(UUIDTimeStampModel):
    title = models.CharField(max_length=100, verbose_name='title')
    rating = models.IntegerField(null=True,
                                 verbose_name='total team rating')
    competition = models.ManyToManyField(Application,
                                         verbose_name='competition')


class Referee(UUIDTimeStampModel):
    class Roles(Enum):
        first = ('1st', 'First')
        second = ('2nd', 'Second')
        scorer = ('scr', 'Scorer')
        line_judge = ('lnj', 'Line judge')

    user = models.UUIDField(verbose_name='users uuid', unique=True)
    game = models.ManyToManyField(Game)
    role = models.CharField(max_length=3,
                            choices=[x.value for x in Roles],
                            verbose_name='role')
