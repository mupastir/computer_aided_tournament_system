from django.test import TestCase
from participant.models import Referee
from participant.services.is_referee import is_referee
from user_auth.models import User


class RefereeCheckTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_r = User.objects.create_user('user_r',
                                              'user_r@gmail.com',
                                              'top_secure')
        cls.user_n = User.objects.create_user('user_n',
                                              'user_n@gmail.com',
                                              'top_secure')
        Referee.objects.create(user_id=cls.user_r.id)

    def test_is_referee_user(self):
        assert is_referee(self.user_r.id)
        assert not is_referee(self.user_n.id)
