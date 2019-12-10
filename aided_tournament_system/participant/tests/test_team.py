from competition.choices import CompetitionTypeChoices
from django.test import TestCase
from participant.models import Player, Team
from participant.services.player import add_rating_to_player
from participant.services.team import add_player, team_rating_calculate
from user_auth.models import User


class TeamActionsTestCases(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_1 = User.objects.create_user(username='test1',
                                              email="test1@test.com",
                                              password="top_secure",
                                              gender="m")
        cls.user_2 = User.objects.create_user(username='test2',
                                              email="test2@test.com",
                                              password="top_secure",
                                              gender="m")
        cls.player_1 = Player.objects.create(user_id=cls.user_1.id)
        cls.player_2 = Player.objects.create(user_id=cls.user_2.id)
        add_rating_to_player(cls.player_1)
        add_rating_to_player(cls.player_2)
        cls.team = Team.objects.create(title="test")

    def test_add_player_to_team(self):
        add_player(self.team.id, self.user_1.id)
        add_player(self.team.id, self.user_2.id)
        assert self.player_1 in self.team.players.all()
        assert self.player_2 in self.team.players.all()

    def test_team_rating_calculate(self):
        add_player(self.team.id, self.user_1.id)
        add_player(self.team.id, self.user_2.id)
        player_1_rating = self.player_1.rating.filter(
            type=CompetitionTypeChoices.BEACH_VOLLEY.value)
        player_1_rating.update(points=7)
        team_rating_calculate(
            team_id=self.team.id,
            competition_type=CompetitionTypeChoices.BEACH_VOLLEY.value
        )
        assert Team.objects.last().rating == 7
