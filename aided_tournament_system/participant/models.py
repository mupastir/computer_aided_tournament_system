from competition.choices import CompetitionTypeChoices
from django.db import models
from django_utils.models import UUIDTimeStampModel
from game.models import Game
from participant.choices import RefereeRoles
from user_auth.models import User

from .managers import PlayerManager


class Player(UUIDTimeStampModel):
    user = models.ForeignKey(
        "user_auth.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="user",
        related_name="players",
    )
    rating = models.ManyToManyField(
        "Rating", blank=True, verbose_name="rating", related_name="players"
    )
    team = models.ManyToManyField(
        "Team", blank=True, verbose_name="team", related_name="players"
    )
    objects = PlayerManager()

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"

    class Meta:
        db_table = "player"


class Rating(UUIDTimeStampModel):
    type = models.CharField(
        choices=CompetitionTypeChoices.get_choices(),
        max_length=40,
        verbose_name="type rating",
    )
    points = models.IntegerField(verbose_name="points")

    class Meta:
        db_table = "rating"


class Team(UUIDTimeStampModel):
    title = models.CharField(max_length=100, verbose_name="title")
    rating = models.IntegerField(
        blank=True, null=True, verbose_name="total team rating"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "team"


class Referee(UUIDTimeStampModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="referees"
    )
    game = models.ManyToManyField(Game)
    role = models.CharField(
        max_length=3, choices=RefereeRoles.get_choices(), verbose_name="role"
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = "referee"
