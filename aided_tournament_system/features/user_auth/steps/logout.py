from behave import given, then, when
from rest_framework.test import APIClient

client = APIClient()


@given("Logged in user")
def get_logged_in_user(context):
    context.execute_steps(
        """
        given Existing user
        when User login existing user
    """
    )


@when("Try to logout user")
def logout_user(context):
    context.response = client.post("/api/user/logout/")


@then("I get successfully logout")
def successfully_logout(context):
    assert context.response.json()["detail"] == "Successfully logged out."
