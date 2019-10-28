import uuid as uuid_lib
from enum import Enum

from competition.models import Application
from django.db import models
from django_countries.fields import CountryField
from game.models import Game
from user_auth.models import User


class Player(User):
    class GENDER(Enum):
        woman = ('w', 'Woman')
        man = ('m', 'Man')

    gender = models.CharField(max_length=1,
                              choices=[x.value for x in GENDER],
                              verbose_name='sex')
    country = CountryField(blank_label='(select country)',
                           verbose_name='country')
    rating = models.IntegerField(null=True,
                                 verbose_name='rating')
    team = models.ManyToManyField('Team',
                                  verbose_name='team')


class Team(models.Model):
    uuid = models.UUIDField(db_index=True,
                            default=uuid_lib.uuid4,
                            editable=False,
                            primary_key=True,
                            verbose_name='uuid')
    title = models.CharField(max_length=100, verbose_name='title')
    rating = models.IntegerField(null=True,
                                 verbose_name='total team rating')
    competition = models.ManyToManyField(Application,
                                         verbose_name='competition')


class Referee(User):
    class Roles(Enum):
        first = ('1st', 'First')
        second = ('2nd', 'Second')
        scorer = ('scr', 'Scorer')
        line_judge = ('lnj', 'Line judge')

    game = models.ManyToManyField(Game)
    role = models.CharField(max_length=3,
                            choices=[x.value for x in Roles],
                            verbose_name='role')
