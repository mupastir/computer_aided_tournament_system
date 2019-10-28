import uuid as uuid_lib

from competition.models import Competition
from django.db import models
from participant.models import Team


class Game(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid'
    )
    start_time = models.DateTimeField(verbose_name='time start')
    end_time = models.DateTimeField(verbose_name='time end')
    round_game = models.CharField(max_length=7, verbose_name='round')
    game_number = models.IntegerField(verbose_name='number of the game')
    court_number = models.IntegerField(verbose_name='court number')
    owner_team = models.ForeignKey(Team,
                                   on_delete=models.SET_NULL,
                                   related_name='owner',
                                   verbose_name='team which plays at home',
                                   blank=True,
                                   null=True)
    guest_team = models.ForeignKey(Team,
                                   on_delete=models.SET_NULL,
                                   related_name='guests',
                                   verbose_name='team which plays visiting',
                                   blank=True,
                                   null=True)
    winner_score = models.IntegerField(blank=True,
                                       null=True,
                                       verbose_name='winner score')
    loser_score = models.IntegerField(blank=True,
                                      null=True,
                                      verbose_name='winner_score')
    competition = models.ForeignKey(Competition,
                                    on_delete=models.CASCADE,
                                    verbose_name='competition')
