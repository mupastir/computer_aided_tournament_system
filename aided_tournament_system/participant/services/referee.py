from uuid import UUID

from participant.models import Referee


def create_referee(user_id: UUID):
    Referee.objects.create(user_id=user_id)


def is_referee(user_id: UUID) -> bool:
    try:
        Referee.objects.get(user_id=user_id)
        return True
    except Referee.DoesNotExist:
        return False
