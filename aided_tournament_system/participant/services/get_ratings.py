from django.db.models import QuerySet
from django.urls import reverse_lazy
from participant.models import Player
from user_auth.models import User


def get_rating_url(rating_type: str, gender: str):
    return reverse_lazy(
        'ratings',
        kwargs={'type': rating_type,
                'gender': gender}
    )


def get_ratings_by_type_gender(rating_type: str, gender: str) -> QuerySet:
    users_ids = User.objects.filter(
        gender=gender
    ).values_list('id', flat=True)
    return Player.objects.filter(
        user_id__in=users_ids,
        rating__type=rating_type
    ).order_by('-rating__points')
