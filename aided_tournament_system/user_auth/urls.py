from django.conf.urls import url
from rest_auth.registration.views import (SocialAccountDisconnectView,
                                          SocialAccountListView)

from .api import views

urlpatterns = [
    # /user/
    url(
        regex=r'^details/$',
        view=views.UserListAPIView.as_view(),
        name='user_rest_api',
    ),
    url(
        regex=r'^edit/$',
        view=views.UserUpdateAPIView.as_view(),
        name='user_rest_api',
    ),
    url(
        regex=r'^login/$',
        view=views.UserLoginAPIView.as_view(),
        name='user_rest_api',
    ),
    url(
        regex=r'^logout/$',
        view=views.UserLogoutAPIView.as_view(),
        name='user_rest_api',
    ),
    url(
        regex=r'^register/$',
        view=views.UserRegisterAPIView.as_view(),
        name='user_rest_api',
    ),
    url(regex=r'^facebook/connect/$',
        view=views.FacebookConnect.as_view(),
        name='fb_connect'),
    url(regex=r'^google/connect/$',
        view=views.GoogleConnect.as_view(),
        name='g_connect'),
    url(regex=r'^instagram/connect/$',
        view=views.InstagramConnect.as_view(),
        name='inst_connect'),
    url(
        regex=r'^socialaccounts/$',
        view=SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    url(
        regex=r'^socialaccounts/(?P<pk>\d+)/disconnect/$',
        view=SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    )
]
