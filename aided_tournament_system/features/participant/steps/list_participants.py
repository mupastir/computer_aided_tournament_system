from behave import given, when
from features.utils import api_get
from participant.models import Player, Team
from user_auth.models import User


@given('{team_title} with players')
def create_team_with_players(context, team_title):
    team = Team.objects.create(title=team_title)
    for row in context.table:
        user = User.objects.create_user(username=row['username'],
                                        email=row['email'],
                                        password=row['password'],
                                        first_name=row['first_name'],
                                        last_name=row['last_name'])
        player = Player.objects.create(user_id=user.id)
        player.team.add(team)


@when('User check list of teams')
def get_list_teams(context):
    context.response = api_get(
        '/api/participant/team/detail/',
        context.user)


@when('User check list of referees')
def get_list_referees(context):
    context.response = api_get(
        '/api/participant/team/detail/',
        context.user)


@when('User check list of players')
def get_list_players(context):
    context.response = api_get(
        '/api/participant/team/detail/',
        context.user)


@when('User check list of players for a {team}')
def get_players_for_a_team(context, team):
    context.response = api_get(
        f'/api/participant/{team}/players/',
        context.user
    )
