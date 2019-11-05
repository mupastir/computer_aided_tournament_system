from behave import given, then, when

from features.utils import api_post
from participant.models import Player, Referee, Team
from user_auth.models import User


@when('User add player role')
def add_player(context):
    context.response = api_post('/participant/player/add',
                                context.user)


@when('User add referee role')
def add_referee(context):
    context.response = api_post('/participant/referee/add',
                                context.user)


@when('User create {team_title}')
def add_team(context, team_title):
    context.response = api_post('/participant/team/create',
                                context.user,
                                {
                                    'title': team_title
                                })


@given('Players')
def create_players(context):
    context.players = []
    for row in context.table:
        user = User.objects.create_user(username=row['username'],
                                        email=row['email'],
                                        password=row['password'],
                                        first_name=row['first_name'],
                                        last_name=row['last_name'])
        context.players.append(Player.objects.create(user=user.id))


@when('User add {player_username} to {team_title}')
def add_players_to_team(context, player_username, team_title):
    context.response = api_post(f'/participant/{team_title}/add_player',
                                context.user,
                                {
                                    'player_username': player_username
                                })


@given('The {team_title}')
def create_team(context, team_title):
    Team.objects.create(title=team_title)


@then('{team_title} has {player_username}')
def check_team_has_player(context, team_title, player_username):
    player = Player.objects.all()
    team = Team.objects.get(title=team_title)
    assert True is False


@then('User become a player')
def check_player_exist(context):
    user = context.user
    players = Player.objects.all()
    assert True is False


@then('User become a referee')
def check_referee_exist(context):
    user = context.user
    referees = Referee.objects.all()
    assert True is False
