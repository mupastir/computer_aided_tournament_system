from behave import given, then, when
from features.utils import api_post, api_put
from participant.models import Player, Referee, Team


@when('User add player role')
def add_player(context):
    context.response = api_post('/api/participant/players/',
                                context.user)


@when('User add referee role')
def add_referee(context):
    context.response = api_post('/api/participant/referees/',
                                context.user)


@when('User create {team_title}')
def add_team(context, team_title):
    context.response = api_post('/api/participant/teams/',
                                context.user,
                                {
                                    'title': team_title
                                })


@given('Player is user')
def create_players(context):
    Player.objects.create(user_id=context.user.id)


@when('User try to join to {team_title}')
def add_players_to_team(context, team_title):
    player = Player.objects.get(user=context.user)
    team = Team.objects.first()
    context.response = api_put(
        f'/api/participant/teams/{team.id}/player/{player.id}/',
        context.user
    )


@given('The {team_title}')
def create_team(context, team_title):
    Team.objects.create(title=team_title)


@then('{team_title} has {player_username}')
def check_team_has_player(context, team_title, player_username):
    assert Player.objects.first().team.first() == Team.objects.first()


@then('User become a player')
def check_player_exist(context):
    assert Player.objects.first().user_id == context.user.id


@then('User become a referee')
def check_referee_exist(context):
    assert Referee.objects.first().user_id == context.user.id
