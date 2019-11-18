from __future__ import absolute_import, unicode_literals

from celery import shared_task
from participant.services.recalculating_player_rating import recalculate_rating


@shared_task
def recalculate_rating_task(competition_type: str):
    recalculate_rating(competition_type)
