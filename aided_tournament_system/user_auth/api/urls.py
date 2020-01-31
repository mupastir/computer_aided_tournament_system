from django.conf.urls import url
from rest_auth.registration.views import (SocialAccountDisconnectView,
                                          SocialAccountListView)
from user_auth.api import views
from user_auth.api.views import (UserPasswordChangeAPIView,
                                 UserPasswordResetAPIView,
                                 UserPasswordResetConfirmAPIView)

app_name = 'api_user'
urlpatterns = [
    # /user/
    url(
        regex=r'^details/$',
        view=views.UserListAPIView.as_view(),
        name='details',
    ),
    url(
        regex=r'^edit/$',
        view=views.UserUpdateAPIView.as_view(),
        name='edit',
    ),
    url(
        regex=r'^login/$',
        view=views.UserLoginAPIView.as_view(),
        name='login',
    ),
    url(
        regex=r'^logout/$',
        view=views.UserLogoutAPIView.as_view(),
        name='logout',
    ),
    url(
        regex=r'^registration/$',
        view=views.UserRegisterAPIView.as_view(),
        name='registration',
    ),
    url(
        regex=r'^password/reset/$',
        view=UserPasswordResetAPIView.as_view(),
        name='password_reset'
    ),
    url(
        regex=r'^password/reset/confirm/$',
        view=UserPasswordResetConfirmAPIView.as_view(),
        name='password_reset_confirm'
    ),
    url(
        regex=r'^password/change/$',
        view=UserPasswordChangeAPIView.as_view(),
        name='password_change'
    ),
    url(regex=r'^facebook/login/$',
        view=views.FacebookLogin.as_view(),
        name='fb_Login'),
    url(regex=r'^google/login/$',
        view=views.GoogleLogin.as_view(),
        name='g_Login'),
    url(regex=r'^instagram/login/$',
        view=views.InstagramLogin.as_view(),
        name='inst_Login'),
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
