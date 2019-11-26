from uuid import UUID

from participant.models import Team


def team_rating_calculate(team_id: UUID, competition_type: str):
    team = Team.objects.get(id=team_id)
    players_queryset = team.player_set.all()
    team.rating = sum([player.rating.get(type=competition_type).points
                       for player in players_queryset])
    team.save()
