from behave import given, then, when


@given('Logged in user')
def get_logged_in_user(context):
    context.execute_steps("""
        given Existing user
        when I login existing user
    """)


@when('Try to logout user')
def logout_user(context):
    context.response = context.test.client.post('/user/logout/')


@then('I get successfully logout')
def successfully_logout(context):
    assert context.response.json()['detail'] == 'Successfully logged out.'
