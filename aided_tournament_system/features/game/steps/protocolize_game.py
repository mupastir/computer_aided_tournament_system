from datetime import datetime, timedelta

from behave import given, then, when
from competition.models import Competition
from features.utils import api_put
from game.models import Game
from participant.models import Player, Referee
from user_auth.models import User


@given('{username} with role {role}')
def referee_scorer(context, username, role):
    context.user = User.objects.create_user(username=username,
                                            email=username + '@gmail.com',
                                            password='top_secure')
    Referee.objects.create(user_id=context.user.id,
                           role=role)


@given('Player')
def create_player(context):
    context.user = User.objects.create_user(username='test',
                                            email='test@gmail.com',
                                            password='top_secure')
    Player.objects.create(user_id=context.user.id)


@given('{game_round} for competition {comp_title}')
def create_competition(context, game_round, comp_title):
    competition = Competition.objects.create(
        title=comp_title,
        start_time=datetime.now(),
        end_time=datetime.now() + timedelta(days=2.0),
        courts_number=2,
        schedule_system='8')
    teams = {}
    for row in context.table:
        teams[row['status']] = row['team']
    Game.objects.create(start_time=datetime.now(),
                        round_game=game_round,
                        competition=competition,
                        game_number=1,
                        court_number=1,
                        home_team=teams['home'],
                        away_team=teams['away'])


@when('User protocolized score {home_team_score} - {away_team_score}')
def protocolized_score(context, home_team_score, away_team_score):
    context.response = api_put(
        f'/game/{Game.objects.first().id}/update_score/',
        context.user,
        {
            'home_team_score': home_team_score,
            'away_team_score': away_team_score,
        })


@then("Error user doesn't have permission")
def check_winner(context):
    assert context.response.status_code == 403
