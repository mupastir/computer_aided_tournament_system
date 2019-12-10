from uuid import UUID

from participant.models import Player, Team


def team_rating_calculate(team_id: UUID, competition_type: str):
    team = Team.objects.filter(id=team_id)
    players_queryset = team[0].players.all()
    team.update(rating=sum([player.rating.get(type=competition_type).points
                            for player in players_queryset]))


def add_player(team_id: UUID, user_id: UUID):
    team = Team.objects.get(id=team_id)
    player = Player.objects.get(user_id=user_id)
    player.save()
    player.team.add(team)
