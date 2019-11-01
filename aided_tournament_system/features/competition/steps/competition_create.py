from datetime import datetime

from behave import given, then, when
from game.models import Game


@given('Admin user')
def create_superuser(context):
    pass


@when('I create competition with valid data')
def create_competition_with_valid_data(context):
    context.response = context.test.client.post(
        '/competition/create/',
        {
            'title': 'Test',
            'start_time': datetime.now(),
            'end_time': datetime.now(),
            'courts_number': 4,
            'schedule_system': '32',
            'gender': 'm'
        }
    )


@then('Competition is successfully created')
def is_competition_created(context):
    assert context.response.status_code == 201


@then('Games are created for competition')
def are_games_created(context):
    assert len(Game.objects.all()) > 0


@when('I create competition with invalid data')
def create_invalid_competition(context):
    context.response = context.test.client.post(
        '/competition/create/',
        {
            'title': 'Test',
            'start_time': datetime.now(),
            'courts_number': 4,
            'schedule_system': '32',
            'gender': 'm'
        }
    )


@then('Competition is not created')
def is_competition_created(context):
    assert context.response.status_code == 301
