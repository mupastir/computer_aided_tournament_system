from datetime import datetime, timedelta

from competition.choices import CompetitionTypeChoices, GenderChoices
from competition.models import Competition, Ranking
from django.test import TestCase
from participant.models import Player, Team
from participant.services.get_ratings import (get_rating_for_player,
                                              get_ratings_by_type_gender)
from participant.services.player import (add_rating_to_player, create_player,
                                         recalculate_rating)
from participant.services.team import add_player
from user_auth.models import User


class RatingActionsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test',
                                            email="test@test.com",
                                            password="top_secure",
                                            gender="m")
        cls.player = Player.objects.create(user_id=cls.user.id)
        cls.WON_POINTS = 9

    def test_create_player(self):
        user = User.objects.create_user(username='test1',
                                        email="test1@test.com",
                                        password="top_secure",
                                        gender="m")
        create_player(user_id=user.id)
        player = Player.objects.get(user_id=user.id)
        assert player.user_id == user.id
        assert player.rating.filter(
            type=CompetitionTypeChoices.BEACH_VOLLEY.value
        )[0].points == 0
        assert player.rating.filter(
            type=CompetitionTypeChoices.PARK_VOLLEY.value
        )[0].points == 0

    def test_add_rating_to_player(self):
        add_rating_to_player(self.player)
        assert self.player.rating.filter(
            type=CompetitionTypeChoices.BEACH_VOLLEY.value
        )[0].points == 0
        assert self.player.rating.filter(
            type=CompetitionTypeChoices.PARK_VOLLEY.value
        )[0].points == 0

    def test_getting_rating_for_player(self):
        add_rating_to_player(self.player)
        assert get_rating_for_player(
            self.player,
            CompetitionTypeChoices.PARK_VOLLEY.value
        ) == 0
        assert get_rating_for_player(
            self.player,
            CompetitionTypeChoices.BEACH_VOLLEY.value
        ) == 0

    def test_getting_rating_by_type_and_gender(self):
        add_rating_to_player(self.player)
        competition_type = CompetitionTypeChoices.BEACH_VOLLEY.value
        gender = GenderChoices.MAN.value
        assert get_ratings_by_type_gender(
            competition_type,
            gender
        )[0].rating.get(type=competition_type).points == 0
        assert get_ratings_by_type_gender(
            competition_type,
            gender
        )[0].rating.get(
            type=CompetitionTypeChoices.BEACH_VOLLEY.value
        ).points == 0

    def test_recalculate_rating(self):
        user = User.objects.create_user(username='test1',
                                        email="test1@test.com",
                                        password="top_secure",
                                        gender="m")
        create_player(user_id=user.id)
        player = Player.objects.get(user_id=user.id)
        competition = Competition.objects.create(
            type=CompetitionTypeChoices.BEACH_VOLLEY.value,
            start_time=datetime.now(),
            end_time=datetime.now()+timedelta(days=2.0),
            courts_number=2
        )
        team = Team.objects.create(title="test")
        add_player(team_id=team.id, user_id=user.id)
        Ranking.objects.create(competition=competition,
                               team=team,
                               place=1,
                               ranking=self.WON_POINTS)
        recalculate_rating(CompetitionTypeChoices.BEACH_VOLLEY.value)
        assert player.rating.get(type="Beach").points == self.WON_POINTS
