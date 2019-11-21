from __future__ import absolute_import, unicode_literals

from uuid import UUID

from celery import shared_task
from participant.models import Player, Referee, Team
from participant.services.add_rating_to_player import add_rating_to_player
from participant.services.recalculating_player_rating import recalculate_rating


@shared_task
def recalculate_rating_task(competition_type: str):
    recalculate_rating(competition_type)


@shared_task
def create_referee_task(user_id: UUID):
    Referee.objects.create(user_id=user_id)


@shared_task
def create_player_task(user_id: UUID):
    player = Player.objects.create(user_id=user_id)
    add_rating_to_player(player)


@shared_task
def player_join_team_task(team_id: UUID, user_id: UUID):
    team = Team.objects.get(id=team_id)
    player = Player.objects.get(user_id=user_id)
    player.save()
    player.team.add(team)
