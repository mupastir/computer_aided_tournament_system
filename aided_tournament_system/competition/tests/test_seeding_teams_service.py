from datetime import datetime

from competition.models import Application, Competition
from competition.services.seeding_teams_service import SeedingTeamsService
from django.test import TestCase
from game.models import Game
from game.services.schedule_creation_services.schedule_creator import \
    ScheduleCreator
from participant.models import Team


class SeedingTeamsTestCase(TestCase):

    def test_seeding_teams(self):
        Team.objects.bulk_create([
            Team(title='indigo', rating=20),
            Team(title='malvin', rating=18),
            Team(title='cristal', rating=25),
            Team(title='croissant', rating=12),
            Team(title='cookie', rating=8),
            Team(title='carrot', rating=33),
            Team(title='beluga', rating=2)
        ])
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='8',
                                                 gender='m')
        schedule_creator = ScheduleCreator(competition.schedule_system,
                                           competition.id)
        schedule_creator.create_schedule()
        for team in Team.objects.all():
            Application.objects.create(competition=competition,
                                       team=team)
        seeding_teams_service = SeedingTeamsService(competition.id)
        seeding_teams_service.seed()

        assert (Game.objects.get(competition=competition,
                                 game_number=1).home_team
                == Team.objects.get(title='carrot').id)
        assert (Game.objects.get(competition=competition,
                                 game_number=1).away_team
                is None)

        assert (Game.objects.get(competition=competition,
                                 game_number=2).home_team
                == Team.objects.get(title='cristal').id)
        assert (Game.objects.get(competition=competition,
                                 game_number=2).away_team
                == Team.objects.get(title='beluga').id)

        assert (Game.objects.get(competition=competition,
                                 game_number=3).home_team
                == Team.objects.get(title='indigo').id)
        assert (Game.objects.get(competition=competition,
                                 game_number=3).away_team
                == Team.objects.get(title='cookie').id)

        assert (Game.objects.get(competition=competition,
                                 game_number=4).home_team
                == Team.objects.get(title='malvin').id)
        assert (Game.objects.get(competition=competition,
                                 game_number=4).away_team
                == Team.objects.get(title='croissant').id)
