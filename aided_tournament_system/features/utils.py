from rest_framework.test import APIClient


def force_authenticated(method: callable):
    def wrapper(path, user, *args, **kwargs):
        client = APIClient()
        client.force_authenticate(user)
        return method(path, client, *args, **kwargs)

    return wrapper


@force_authenticated
def api_get(path, client, *args, **kwargs):
    return client.get(path, *args, **kwargs)


@force_authenticated
def api_post(path, client, *args, **kwargs):
    return client.post(path, *args, **kwargs)


@force_authenticated
def api_put(path, client, *args, **kwargs):
    return client.put(path, *args, **kwargs)


@force_authenticated
def api_patch(path, client, *args, **kwargs):
    return client.patch(path, *args, **kwargs)
