from django.conf.urls import url

from .api import views

urlpatterns = [
    # /user/
    url(
        regex=r'^$',
        view=views.UserListAPIView.as_view(),
        name='user_rest_api',
    ),
    url(
        regex=r'^create/$',
        view=views.UserCreateAPIView.as_view(),
        name='user_rest_api',
    ),
]
