from datetime import datetime

from competition.models import Competition
from django.test import TestCase
from game.models import Game
from game.services.schedule_creation_service import Tournament32Teams


class TestScheduleCreatingService(TestCase):

    def test_create_30_games(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='32',
                                                 gender='m')
        tournament_32_team = Tournament32Teams()
        tournament_32_team.create_games_schedule(competition.pk)
        assert len(Game.objects.all()) == 30
