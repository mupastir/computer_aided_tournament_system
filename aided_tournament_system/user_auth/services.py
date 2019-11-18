from uuid import UUID

from django.db.models import QuerySet
from user_auth.models import User


def get_user_by_id(user_id: UUID) -> QuerySet:
    return User.objects.get(id=user_id)
