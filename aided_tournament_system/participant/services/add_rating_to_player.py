from competition.choices import CompetitionTypeChoices
from participant.models import Player, Rating


def add_rating_to_player(player: Player):
    ratings_list = Rating.objects.bulk_create([
        Rating(type=CompetitionTypeChoices.BEACH_VOLLEY.value),
        Rating(type=CompetitionTypeChoices.PARK_VOLLEY.value)
    ])
    player.rating.add(ratings_list)
