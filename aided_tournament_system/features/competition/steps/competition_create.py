from ast import literal_eval
from datetime import datetime

from behave import given, then, when
from features.utils import api_post
from game.models import Game
from participant.models import Referee
from user_auth.models import User


@given('User with email: {email} and password: {password}, '
       'superuser: {is_superuser}, staff: {is_staff}.')
def create_superuser(context, email, password, is_superuser, is_staff):
    context.user = User.objects.create_superuser(
        username=email,
        password=password,
        email=email,
        is_superuser=literal_eval(is_superuser),
        is_staff=literal_eval(is_staff)
    )


@given('Referee with First name: {first_name}, Last name: {last_name}, '
       'username: {username}, email: {email}, password: {password}.')
def create_referee(context, first_name, last_name, username, email, password):
    user = User.objects.create_superuser(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    Referee.objects.create(user=user)


@when('User creates competition with valid data')
def create_competition_with_valid_data(context):
    context.response = api_post(
        '/api/competition/create/',
        context.user,
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
def check_competition_created(context):
    assert context.response.status_code == 201


@then('Games are created for competition')
def check_games_created(context):
    assert len(Game.objects.all()) > 0


@when('User creates competition with invalid data')
def create_invalid_competition(context):
    context.response = api_post(
        '/api/competition/create/',
        context.user,
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
    assert context.response.status_code == 400
