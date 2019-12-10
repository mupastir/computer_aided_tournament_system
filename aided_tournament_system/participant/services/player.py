from uuid import UUID

from competition.choices import CompetitionTypeChoices
from competition.models import Competition, Ranking
from django.db.models import Sum
from participant.models import Player, Rating


def add_rating_to_player(player: Player):
    ratings_list = Rating.objects.bulk_create([
        Rating(type=CompetitionTypeChoices.BEACH_VOLLEY.value, points=0),
        Rating(type=CompetitionTypeChoices.PARK_VOLLEY.value, points=0)
    ])
    player.rating.add(*ratings_list)


def create_player(user_id: UUID):
    player = Player.objects.create(user_id=user_id)
    add_rating_to_player(player)


def recalculate_rating(competition_type: str):
    competition_ids = list(
        Competition.objects.filter(
            type=competition_type
        ).order_by('-created')[:6].values_list('id', flat=True)
    )

    for player in Player.objects.all():
        query_rating = Ranking.objects.filter(
            competition_id__in=competition_ids,
            team__players__id=player.id
        ).aggregate(Sum('ranking'))
        player_rating = player.rating.filter(type=competition_type)
        player_rating.update(points=query_rating['ranking__sum'] or 0)
