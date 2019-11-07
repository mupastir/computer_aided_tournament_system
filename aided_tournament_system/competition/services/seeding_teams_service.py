from uuid import UUID

from competition.models import Competition
from django.db.models import QuerySet
from game.models import Game
from participant.models import Team


class SeedingTeamsService:

    def __init__(self, competition_id: UUID):
        self.competition_id = competition_id
        self.competition = self._get_competition()
        self.teams_number = self._get_teams_number()

    def _get_competition(self) -> Competition:
        return Competition.objects.get(id=self.competition_id)

    def _get_teams(self) -> QuerySet:
        return Team.objects \
                   .filter(applications__competition=self.competition) \
                   .order_by('-rating')[:self.teams_number]

    def _get_teams_number(self) -> int:
        return int(self.competition.schedule_system)

    def seed(self):
        """
        Team with the most rating will play with the least rating team,
        team on the 2 second place - with pre last team and so on
        ratings = [25, 23, 18, 6, 3, ]
        25 - None
        23 - 3
        18 - 6
        :return:
        """
        teams = self._get_teams()

        for i in range(self.teams_number // 2):
            try:
                away_team = teams[self.teams_number - 1 - i].id
            except IndexError:
                away_team = None
            Game.objects.filter(competition=self.competition,
                                game_number=i + 1).update(
                home_team_id=teams[i].id,
                away_team_id=away_team)
