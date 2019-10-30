from competition.models import Competition
from django.db import models
from django_utils.models import UUIDTimeStampModel


class Game(UUIDTimeStampModel):
    start_time = models.DateTimeField(verbose_name='time start')
    end_time = models.DateTimeField(verbose_name='time end')
    round_game = models.CharField(max_length=7, verbose_name='round')
    game_number = models.IntegerField(verbose_name='number of the game')
    court_number = models.IntegerField(verbose_name='court number')
    owner_team = models.ForeignKey('participant.Team',
                                   on_delete=models.SET_NULL,
                                   related_name='owner',
                                   verbose_name='team which plays at home',
                                   blank=True,
                                   null=True)
    guest_team = models.ForeignKey('participant.Team',
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
