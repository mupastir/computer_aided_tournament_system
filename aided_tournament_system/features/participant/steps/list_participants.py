from behave import given, then, when
from competition.choices import CompetitionTypeChoices
from features.utils import api_get
from participant.models import Player, Rating, Team
from user_auth.models import User


@given("{team_title} with players")
def create_team_with_players(context, team_title):
    team = Team.objects.create(title=team_title)
    ratings = 0
    for row in context.table:
        rating = Rating.objects.create(
            type=CompetitionTypeChoices.BEACH_VOLLEY.value,
            points=int(row["beach_rating"]),
        )
        user = User.objects.create_user(
            username=row["username"],
            email=row["email"],
            password=row["password"],
            first_name=row["first_name"],
            last_name=row["last_name"],
        )
        player = Player.objects.create(user=user)
        player.rating.add(rating)
        ratings += rating.points
        player.team.add(team)
    team.rating = ratings
    team.save()


@when("User check list of teams")
def get_list_teams(context):
    context.response = api_get("/api/participant/teams/", context.user)


@when("User check list of referees")
def get_list_referees(context):
    context.response = api_get("/api/participant/referees/", context.user)


@when("User check list of players")
def get_list_players(context):
    context.response = api_get("/api/participant/players/", context.user)


@when("User check list of players for a {team}")
def get_players_for_a_team(context, team):
    context.response = api_get(f"/api/participant/{team}/players/", context.user)


@then("Get teams info correct")
def get_team_list(context):
    data = context.response.json()
    assert data[0]["title"] == "Team"
    assert data[0]["rating"] == 17
    assert data[0]["players"][0]["user"]["first_name"] == "Masha"
    assert data[0]["players"][1]["user"]["first_name"] == "Misha"
    assert data[0]["players"][0]["user"]["username"] == "test1"
    assert data[0]["players"][1]["user"]["username"] == "test2"
    assert data[0]["players"][0]["user"]["last_name"] == "Test"
    assert data[0]["players"][1]["user"]["last_name"] == "Test"
    assert data[0]["players"][0]["user"]["email"] == "test@test.com"
    assert data[0]["players"][1]["user"]["email"] == "test@test.com"
    assert data[0]["players"][0]["rating"][0]["type"] == "Beach"
    assert data[0]["players"][1]["rating"][0]["type"] == "Beach"
    assert data[0]["players"][0]["rating"][0]["points"] == 5
    assert data[0]["players"][1]["rating"][0]["points"] == 12


@then("Get referee info correct")
def get_referee_list(context):
    data = context.response.json()
    assert data[0]["user"]["first_name"] == "Sergey"
    assert data[0]["user"]["last_name"] == "Pupkin"
    assert data[0]["user"]["username"] == "pupkin"
    assert data[0]["user"]["email"] == "test@test.com"


@then("Get users info correct")
def get_players_list(context):
    data = context.response.json()
    assert data[0]["user"]["first_name"] == "Masha"
    assert data[1]["user"]["first_name"] == "Misha"
    assert data[0]["user"]["username"] == "test1"
    assert data[1]["user"]["username"] == "test2"
    assert data[0]["user"]["last_name"] == "Test"
    assert data[1]["user"]["last_name"] == "Test"
    assert data[0]["user"]["email"] == "test@test.com"
    assert data[1]["user"]["email"] == "test@test.com"
    assert data[0]["rating"][0]["type"] == "Beach"
    assert data[1]["rating"][0]["type"] == "Beach"
    assert data[0]["rating"][0]["points"] == 5
    assert data[1]["rating"][0]["points"] == 12
