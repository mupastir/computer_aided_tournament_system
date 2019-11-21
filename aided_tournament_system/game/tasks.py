from uuid import UUID

from celery import shared_task
from game.services.round_moving_service import RoundMovingService


@shared_task
def move_teams_next_round_task(game_id: UUID):
    round_moving_service = RoundMovingService(game_id)
    round_moving_service.move_teams()
