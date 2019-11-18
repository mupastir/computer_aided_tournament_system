from django.db.models import Prefetch, QuerySet
from django.urls import reverse_lazy
from participant.models import Player, Rating
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
    return Player.objects.prefetch_related(
        Prefetch('rating',
                 queryset=Rating.objects.filter(type=rating_type),
                 to_attr="player_rating")
    ).filter(user_id__in=users_ids,
             rating__type=rating_type).order_by('-rating__points')


def get_rating_for_player(player: Player, rating_type: str):
    return player.rating.filter(
        type=rating_type)[0].points
