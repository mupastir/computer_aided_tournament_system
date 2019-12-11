from datetime import datetime

from competition.models import Competition, Ranking
from competition.services.constants import (Ranking8Teams, Ranking16Teams,
                                            Ranking32Teams)
from competition.services.ranking import ranking_creating_service
from django.test import TestCase


class TestRankingsCreateService(TestCase):

    def test_rankings_for_8_teams_creation(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='8',
                                                 gender='m')
        ranking_creating_service(competition_id=competition.id)
        assert len(Ranking.objects.all()) == 8
        assert Ranking.objects.get(
            place=1,
            competition=competition
        ).ranking == Ranking8Teams.FIRST_PLACE
        assert Ranking.objects.get(
            place=2,
            competition=competition
        ).ranking == 5
        assert Ranking.objects.get(
            place=3,
            competition=competition
        ).ranking == 4
        assert Ranking.objects.get(
            place=4,
            competition=competition
        ).ranking == 3
        assert Ranking.objects.filter(
            place=5,
            competition=competition
        ).first().ranking == Ranking8Teams.FIFTH_PLACE
        assert Ranking.objects.filter(
            place=7,
            competition=competition
        ).first().ranking == Ranking8Teams.SEVENTH_PLACE

    def test_rankings_for_16_teams_creation(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='16',
                                                 gender='m')
        ranking_creating_service(competition_id=competition.id)
        assert len(Ranking.objects.all()) == 16
        assert Ranking.objects.get(
            place=1,
            competition=competition
        ).ranking == Ranking16Teams.FIRST_PLACE
        assert Ranking.objects.get(
            place=2,
            competition=competition
        ).ranking == 7
        assert Ranking.objects.get(
            place=3,
            competition=competition
        ).ranking == 6
        assert Ranking.objects.get(
            place=4,
            competition=competition
        ).ranking == 5
        assert Ranking.objects.filter(
            place=5,
            competition=competition
        ).first().ranking == Ranking16Teams.FIFTH_PLACE
        assert Ranking.objects.filter(
            place=7,
            competition=competition
        ).first().ranking == Ranking16Teams.SEVENTH_PLACE
        assert Ranking.objects.filter(
            place=9,
            competition=competition
        ).first().ranking == Ranking16Teams.NINTH_PLACE
        assert Ranking.objects.filter(
            place=13,
            competition=competition
        ).first().ranking == Ranking16Teams.THIRTEENTH_PLACE

    def test_rankings_for_32_teams_creation(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='32',
                                                 gender='m')
        ranking_creating_service(competition_id=competition.id)
        assert len(Ranking.objects.all()) == 32
        assert Ranking.objects.get(
            place=1,
            competition=competition
        ).ranking == Ranking32Teams.FIRST_PLACE
        assert Ranking.objects.get(
            place=2,
            competition=competition
        ).ranking == 9
        assert Ranking.objects.get(
            place=3,
            competition=competition
        ).ranking == 8
        assert Ranking.objects.get(
            place=4,
            competition=competition
        ).ranking == 7
        assert Ranking.objects.filter(
            place=5,
            competition=competition
        ).first().ranking == Ranking32Teams.FIFTH_PLACE
        assert Ranking.objects.filter(
            place=7,
            competition=competition
        ).first().ranking == Ranking32Teams.SEVENTH_PLACE
        assert Ranking.objects.filter(
            place=9,
            competition=competition
        ).first().ranking == Ranking32Teams.NINTH_PLACE
        assert Ranking.objects.filter(
            place=13,
            competition=competition
        ).first().ranking == Ranking32Teams.THIRTEENTH_PLACE
        assert Ranking.objects.filter(
            place=17,
            competition=competition
        ).first().ranking == Ranking32Teams.SEVENTEENTH_PLACE
        assert Ranking.objects.filter(
            place=25,
            competition=competition
        ).first().ranking == Ranking32Teams.TWENTY_FIFTH_PLACE
