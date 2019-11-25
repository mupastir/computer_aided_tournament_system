from uuid import UUID

from participant.models import Team


def team_rating_calculate(team_id: UUID):
    # ToDo: rewrite rating calculate
    team = Team.objects.get(id=team_id)
    players_queryset = team.player_set.all()
    team.rating = sum([player.rating for player in players_queryset])
    team.save()
