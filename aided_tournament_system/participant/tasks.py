from __future__ import absolute_import, unicode_literals

from uuid import UUID

from celery import shared_task
from participant.models import Player, Team
from participant.services.recalculating_player_rating import recalculate_rating
from user_auth.models import User


@shared_task
def recalculate_rating_task(competition_type: str):
    recalculate_rating(competition_type)


@shared_task
def player_join_team_task(team_id: UUID, user: User):
    team = Team.objects.get(id=team_id)
    player = Player.objects.get(user=user)
    player.save()
    player.team.add(team)
