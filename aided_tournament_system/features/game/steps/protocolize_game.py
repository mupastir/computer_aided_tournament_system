from datetime import datetime, timedelta

from behave import given, then, when
from rest_framework import status

from competition.models import Competition
from features.utils import api_patch
from game.choices import RoundChoices
from game.models import Game
from participant.models import Player, Referee, Team
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
        Team.objects.create(title=row['team'])
    Game.objects.create(start_time=datetime.now(),
                        round_game=RoundChoices.FINAL_ROUND.value,
                        competition=competition,
                        game_number=1,
                        court_number=1,
                        home_team_id=Team.objects.get(title=teams['home']).id,
                        away_team_id=Team.objects.get(title=teams['away']).id)


@when('User protocolized score {home_team_score} - {away_team_score}')
def protocolized_score(context, home_team_score, away_team_score):
    context.response = api_patch(
        f'/api/game/{Game.objects.first().id}/',
        context.user,
        {
            'home_team_score': home_team_score,
            'away_team_score': away_team_score,
        })


@then("Error user doesn't have permission")
def check_winner(context):
    assert context.response.status_code == status.HTTP_403_FORBIDDEN
