from behave import given, then, when


@given('Existing user')
def existing_user(context):
    context.execute_steps('''
            when I entered a valid user data
        ''')


@when('I login existing user')
def login_existed_user(context):
    context.response = context.test.client.post('/user/login/',
                                                {
                                                    'username': 'test',
                                                    'email': 'test@test.com',
                                                    'password': 'top_secure'
                                                })


@then('I get token of this user')
def get_user_token(context):
    assert len(context.response.json()['key']) > 0


@then('Status code is 200')
def get_success_status_code(context):
    assert context.response.status_code == 200


@when('I login not existing user')
def login_not_existing_user(context):
    context.response = context.test.client.post('/user/login/',
                                                {
                                                    'username': 'est',
                                                    'email': 'est@test.com',
                                                    'password': 'top_secure'
                                                })


@then('I get error message')
def get_error_msg(context):
    print(context.response)
    assert context.response.status_code == 400
