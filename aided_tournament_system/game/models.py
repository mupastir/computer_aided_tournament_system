from django.db import models
from django_utils.models import UUIDTimeStampModel

from .choices import RoundChoices
from .managers import GameManager


class Game(UUIDTimeStampModel):
    start_time = models.DateTimeField(blank=True,
                                      null=True,
                                      verbose_name='time start')
    end_time = models.DateTimeField(blank=True,
                                    null=True,
                                    verbose_name='time end')
    round_game = models.CharField(choices=RoundChoices.get_choices(),
                                  max_length=8,
                                  verbose_name='round')
    game_number = models.IntegerField(verbose_name='number of the game')
    court_number = models.IntegerField(verbose_name='court number',
                                       blank=True,
                                       null=True)
    home_team = models.CharField(max_length=300,
                                 verbose_name='team which plays at home',
                                 blank=True,
                                 null=True)
    away_team = models.CharField(max_length=300,
                                 verbose_name='team which plays visiting',
                                 blank=True,
                                 null=True)
    winner_score = models.IntegerField(blank=True,
                                       null=True,
                                       verbose_name='winner score')
    loser_score = models.IntegerField(blank=True,
                                      null=True,
                                      verbose_name='winner_score')
    competition = models.ForeignKey('competition.Competition',
                                    on_delete=models.CASCADE,
                                    verbose_name='competition')
    winner_ref = models.CharField(blank=True,
                                  null=True,
                                  max_length=3,
                                  verbose_name='winner reference game number')
    loser_ref = models.CharField(blank=True,
                                 null=True,
                                 max_length=3,
                                 verbose_name='loser reference game number')
    objects = GameManager()

    def __str__(self):
        return f'{self.competition.title}: {self.game_number}'

    class Meta:
        db_table = 'game'
