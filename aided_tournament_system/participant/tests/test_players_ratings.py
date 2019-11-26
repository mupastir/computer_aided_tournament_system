from competition.choices import CompetitionTypeChoices, GenderChoices
from django.test import TestCase
from participant.models import Player
from participant.services.add_rating_to_player import add_rating_to_player
from participant.services.get_ratings import (get_rating_for_player,
                                              get_ratings_by_type_gender)
from user_auth.models import User


class RatingActionsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test',
                                            email="test@test.com",
                                            password="top_secure",
                                            gender="m")
        cls.player = Player.objects.create(user_id=cls.user.id)

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
