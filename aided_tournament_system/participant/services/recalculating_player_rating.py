from competition.models import Competition, Ranking
from django.db.models import Sum
from participant.models import Player


def recalculate_rating():
    competition_ids = list(
        Competition.objects.order_by('-created')[:5].values_list('id',
                                                                 flat=True)
    )

    for player in Player.objects.all():
        query_rating = Ranking.objects.filter(
            competition_id__in=competition_ids,
            team__player__id=player.id
        ).aggregate(Sum('ranking'))
        player.rating = query_rating['rating_sum'] or 0
        player.save()
