from competition.models import Competition, Ranking
from django.db.models import Sum
from participant.models import Player


def recalculate_rating(competition_type: str):
    competition_ids = list(
        Competition.objects.filter(
            type=competition_type
        ).order_by('-created')[:6].values_list('id',
                                               flat=True)
    )

    for player in Player.objects.all():
        query_rating = Ranking.objects.filter(
            competition_id__in=competition_ids,
            team__player__id=player.id
        ).aggregate(Sum('ranking'))
        player_rating = player.rating.get(player=player, type=competition_type)
        player_rating.points = query_rating['rating_sum'] or 0
        player_rating.save()
