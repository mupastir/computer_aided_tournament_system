from datetime import datetime

from competition.models import Application, Competition
from competition.services.application_closing_service import \
    ApplicationClosingService
from django.test import TestCase


class TestApplicationClosingService(TestCase):

    def test_closing_application(self):
        competition = Competition.objects.create(title='Test',
                                                 start_time=datetime.now(),
                                                 end_time=datetime.now(),
                                                 courts_number=4,
                                                 schedule_system='32',
                                                 gender='m')
        Application.objects.create(competition=competition)
        application_closer = ApplicationClosingService(competition.id)
        application_closer.close()
        assert Application.objects.first().is_open is False
