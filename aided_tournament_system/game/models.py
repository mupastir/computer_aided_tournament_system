from django.db import models
from django_utils.models import UUIDTimeStampModel
from game.choices import RoundChoices

from .managers import GameManager


class Game(UUIDTimeStampModel):
    start_time = models.DateTimeField(blank=True, null=True, verbose_name="time start")
    end_time = models.DateTimeField(blank=True, null=True, verbose_name="time end")
    round_game = models.CharField(
        choices=RoundChoices.get_choices(), max_length=3, verbose_name="round"
    )
    game_number = models.IntegerField(verbose_name="number of the game")
    court_number = models.IntegerField(
        verbose_name="court number", blank=True, null=True
    )
    home_team = models.ForeignKey(
        "participant.Team",
        verbose_name="team which plays at home",
        related_name="home_team",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    away_team = models.ForeignKey(
        "participant.Team",
        verbose_name="team which plays visiting",
        related_name="away_team",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    home_team_score = models.IntegerField(
        blank=True, null=True, verbose_name="home team score"
    )
    away_team_score = models.IntegerField(
        blank=True, null=True, verbose_name="away team score"
    )
    competition = models.ForeignKey(
        "competition.Competition", on_delete=models.CASCADE, verbose_name="competition"
    )
    winner_ref = models.CharField(
        blank=True, null=True, max_length=3, verbose_name="winner reference game number"
    )
    loser_ref = models.CharField(
        blank=True, null=True, max_length=3, verbose_name="loser reference game number"
    )
    objects = GameManager()

    def __str__(self):
        return f"{self.competition.title}: {self.game_number}"

    class Meta:
        db_table = "game"
