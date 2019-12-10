from __future__ import absolute_import, unicode_literals

from uuid import UUID

from celery import shared_task
from participant.services.player import create_player, recalculate_rating
from participant.services.referee import create_referee
from participant.services.team import add_player


@shared_task
def recalculate_rating_task(competition_type: str):
    recalculate_rating(competition_type)


@shared_task
def create_referee_task(user_id: UUID):
    create_referee(user_id)


@shared_task
def create_player_task(user_id: UUID):
    create_player(user_id)


@shared_task
def player_join_team_task(team_id: UUID, user_id: UUID):
    add_player(team_id=team_id, user_id=user_id)
