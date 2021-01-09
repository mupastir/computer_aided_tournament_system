from competition.choices import CompetitionTypeChoices, GenderChoices
from django.test import TestCase
from participant.models import Player
from participant.services.add_rating_to_player import add_rating_to_player
from participant.services.get_ratings import (get_rating_for_player,
                                              get_players_by_rating_type_and_gender)
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
        competition_beach_type = CompetitionTypeChoices.BEACH_VOLLEY.value
        competition_park_type = CompetitionTypeChoices.PARK_VOLLEY.value
        gender = GenderChoices.MAN.value
        filtered_player_beach = get_players_by_rating_type_and_gender(
            competition_beach_type,
            gender
        )[0]
        filtered_player_park = get_players_by_rating_type_and_gender(
            competition_park_type,
            gender
        )[0]
        assert filtered_player_beach == self.player
        assert filtered_player_park == self.player
        assert filtered_player_beach.player_rating[0].type == competition_beach_type
        assert filtered_player_beach.player_rating[0].points == 0
        assert filtered_player_park.player_rating[0].type == competition_park_type
        assert filtered_player_park.player_rating[0].points == 0
