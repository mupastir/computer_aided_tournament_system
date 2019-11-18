from behave import given, then, when
from rest_framework.test import APIClient

client = APIClient()


@given('Existing user')
def existing_user(context):
    context.execute_steps('''
            when User entered a valid user data
        ''')


@when('User login existing user')
def login_existed_user(context):
    context.response = client.post('/api/user/login/',
                                   {
                                       'username': 'test',
                                       'email': 'test@test.com',
                                       'password': 'top_secure'
                                   })


@then('User get token of this user')
def get_user_token(context):
    assert len(context.response.json()['key']) > 0


@then('Status code is 200')
def get_success_status_code(context):
    assert context.response.status_code == 200


@when('User login not existing user')
def login_not_existing_user(context):
    context.response = client.post('/api/user/login/',
                                   {
                                       'username': 'est',
                                       'email': 'est@test.com',
                                       'password': 'top_secure'
                                   })


@then('User get error message')
def get_error_msg(context):
    print(context.response)
    assert context.response.status_code == 400
