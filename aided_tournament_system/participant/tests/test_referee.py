from django.test import TestCase
from participant.models import Referee
from participant.services.referee import create_referee, is_referee
from user_auth.models import User


class RefereeCheckTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_referee = User.objects.create_user('user_referee',
                                                    'user_referee@gmail.com',
                                                    'top_secure')
        cls.user_not_referee = User.objects.create_user(
            'user_not_referee',
            'user_not_referee@gmail.com',
            'top_secure')

    def test_creation_referee(self):
        create_referee(self.user_referee.id)
        assert Referee.objects.last().user_id == self.user_referee.id

    def test_is_referee_user(self):
        create_referee(self.user_referee.id)
        assert is_referee(self.user_referee.id)
        assert not is_referee(self.user_not_referee.id)
