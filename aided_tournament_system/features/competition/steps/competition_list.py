from datetime import datetime

from behave import given, then, when
from competition.models import Competition
from rest_framework.test import APIClient

client = APIClient()


@given("Existing competitions")
def existing_competition(context):
    Competition.objects.create(
        title="Test",
        start_time=datetime.now(),
        end_time=datetime.now(),
        courts_number=4,
        schedule_system="32",
        gender="m",
    )


@when("Send get request on url /competitions/detail/")
def send_get_request_to_detail(context):
    context.response = context.test.client.get("/api/competition/detail/")


@then("Get list of one existing competition")
def get_list_of_competitions(context):
    assert len(context.response.data) > 0
