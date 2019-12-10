from datetime import datetime

from competition.models import Competition
from django.test import TestCase
from game.models import Game
from game.services.schedule_creation_services.schedule_creator import \
    ScheduleCreator
from game.services.schedule_creation_services.tournament_schedules import (
    Tournament8Teams, Tournament16Teams, Tournament32Teams)


class TestScheduleCreatingService(TestCase):

    def test_fail_teams_creating(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='4',
                                                 gender='m')
        self.assertRaises(ValueError,
                          ScheduleCreator,
                          schedule_size=competition.schedule_system,
                          competition_id=competition.pk)

    def test_create_32_teams_schedule(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='32',
                                                 gender='m')
        tournament_32_team = Tournament32Teams(competition.pk)
        tournament_32_team.create_games_schedule()
        assert len(Game.objects.all()) == 62

    def test_create_16_teams_schedule(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='16',
                                                 gender='m')
        tournament_16_team = Tournament16Teams(competition.pk)
        tournament_16_team.create_games_schedule()
        assert len(Game.objects.all()) == 30

    def test_create_8_teams_schedule(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=2,
                                                 schedule_system='8',
                                                 gender='w')
        tournament_8_team = Tournament8Teams(competition.pk)
        tournament_8_team.create_games_schedule()
        assert len(Game.objects.all()) == 14

    def test_is_created_32_teams_scheduler(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=6,
                                                 schedule_system='32',
                                                 gender='w')
        competition_32_teams = ScheduleCreator(competition.schedule_system,
                                               competition.pk)
        assert competition_32_teams.schedule_creator is Tournament32Teams

    def test_is_created_16_teams_scheduler(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='16',
                                                 gender='w')
        competition_16_teams = ScheduleCreator(competition.schedule_system,
                                               competition.pk)
        assert competition_16_teams.schedule_creator is Tournament16Teams

    def test_is_created_8_teams_scheduler(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=2,
                                                 schedule_system='8',
                                                 gender='w')
        competition_8_teams = ScheduleCreator(competition.schedule_system,
                                              competition.pk)
        assert competition_8_teams.schedule_creator is Tournament8Teams
