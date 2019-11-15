from datetime import datetime

from competition.choices import GenderChoices, ScheduleChoices
from competition.models import Application, Competition
from competition.services.seeding_teams_service import SeedingTeamsService
from django.test import TestCase
from game.models import Game
from game.services.round_moving_service import RoundMovingService
from game.services.schedule_creation_services.schedule_creator import \
    ScheduleCreator
from participant.models import Team


class RoundMovingTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Team.objects.bulk_create([
            Team(title='indigo', rating=20),
            Team(title='malvin', rating=18),
            Team(title='cristal', rating=25),
            Team(title='croissant', rating=12),
            Team(title='cookie', rating=8),
            Team(title='carrot', rating=33),
            Team(title='beluga', rating=2)
        ])
        cls.competition = Competition.objects.create(
            title='Test2',
            start_time=datetime.now(),
            end_time=datetime.now(),
            courts_number=4,
            schedule_system=ScheduleChoices.TEAM_SYSTEM_OF_8.value,
            gender=GenderChoices.MAN.value
        )
        schedule_creator = ScheduleCreator(cls.competition.schedule_system,
                                           cls.competition.id)
        schedule_creator.create_schedule()
        for team in Team.objects.all():
            Application.objects.create(competition=cls.competition,
                                       team=team)
        seeding_teams_service = SeedingTeamsService(cls.competition.id)
        seeding_teams_service.seed()

    def test_round_moving(self):
        Game.objects.filter(game_number=1,
                            competition=self.competition).update(
            home_team_score=2,
            away_team_score=0)
        round_mover = RoundMovingService(
            Game.objects.get(competition=self.competition,
                             game_number=1).id)
        round_mover.move_teams()
        assert Game.objects.get(
            competition=self.competition,
            game_number=5
        ).home_team == Team.objects.get(title='carrot')
        Game.objects.filter(game_number=2,
                            competition=self.competition).update(
            home_team_score=2,
            away_team_score=0
        )
        round_mover = RoundMovingService(
            Game.objects.get(competition=self.competition,
                             game_number=2).id)
        round_mover.move_teams()
        assert Game.objects.get(
            competition=self.competition,
            game_number=5
        ).away_team == Team.objects.get(title='cristal')
        Game.objects.filter(game_number=3,
                            competition=self.competition).update(
            home_team_score=2,
            away_team_score=1
        )
        round_mover = RoundMovingService(
            Game.objects.get(competition=self.competition,
                             game_number=3).id)
        round_mover.move_teams()
        assert Game.objects.get(
            competition=self.competition,
            game_number=6
        ).home_team == Team.objects.get(title='indigo')
        Game.objects.filter(game_number=4,
                            competition=self.competition).update(
            home_team_score=1,
            away_team_score=2
        )
        round_mover = RoundMovingService(
            Game.objects.get(competition=self.competition,
                             game_number=4).id)
        round_mover.move_teams()
        assert Game.objects.get(
            competition=self.competition,
            game_number=6
        ).away_team == Team.objects.get(title='croissant')

        Game.objects.filter(game_number=5,
                            competition=self.competition).update(
            home_team_score=1,
            away_team_score=2
        )
        round_mover = RoundMovingService(
            Game.objects.get(competition=self.competition,
                             game_number=5).id)
        round_mover.move_teams()
        assert Game.objects.get(
            competition=self.competition,
            game_number=11
        ).home_team == Team.objects.get(title='cristal')
        assert Game.objects.get(
            competition=self.competition,
            game_number=9
        ).home_team == Team.objects.get(title='carrot')
        Game.objects.filter(game_number=6,
                            competition=self.competition).update(
            home_team_score=2,
            away_team_score=1
        )
        round_mover = RoundMovingService(
            Game.objects.get(competition=self.competition,
                             game_number=6).id)
        round_mover.move_teams()
        assert Game.objects.get(
            competition=self.competition,
            game_number=12
        ).home_team == Team.objects.get(title='indigo')
        assert Game.objects.get(
            competition=self.competition,
            game_number=10
        ).home_team == Team.objects.get(title='croissant')
