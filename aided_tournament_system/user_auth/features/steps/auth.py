from behave import then, when


@when('I entered a valid user data')
def valid_user_data(context):
    valid_user_data_ = {
        'username': 'test',
        'password1': 'top_secure',
        'password2': 'top_secure',
        'email': 'test@test.com',
        'first_name': 'Test',
        'last_name': 'Test'
    }
    context.response = context.test.client.post('/user/register/',
                                                valid_user_data_)


@then('I got success status code')
def get_success_status_code(context):
    assert context.response.status_code == 201


@when('I entered invalid user data')
def invalid_user_data(context):
    invalid_user_data_ = {
        'username': 'test1',
        'password1': 'top_secure',
        'password2': '123',
        'email': '',
        'first_name': 'Test',
        'last_name': 'Test'
    }
    context.response = context.test.client.post('/user/register/',
                                                invalid_user_data_)


@then('I am got fail status code')
def get_fail_status_code(context):
    print(context.response)
    assert context.response.status_code == 400
