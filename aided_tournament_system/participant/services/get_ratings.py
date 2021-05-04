from django.db.models import Prefetch, QuerySet
from django.urls import reverse_lazy
from participant.models import Player, Rating
from user_auth.models import User


def get_rating_url(rating_type: str, gender: str):
    return reverse_lazy("ratings", kwargs={"type": rating_type, "gender": gender})


def get_players_by_rating_type_and_gender(rating_type: str, gender: str) -> QuerySet:
    return (
        Player.objects.prefetch_related(
            Prefetch(
                "rating",
                queryset=Rating.objects.filter(type=rating_type),
                to_attr="player_rating",
            )
        )
        .filter(user__gender=gender, rating__type=rating_type)
        .order_by("-rating__points")
    )


def get_rating_for_player(player: Player, rating_type: str):
    return player.rating.filter(type=rating_type)[0].points
